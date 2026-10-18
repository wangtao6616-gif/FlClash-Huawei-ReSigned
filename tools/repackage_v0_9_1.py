# SPDX-License-Identifier: GPL-3.0-only
"""Apply the published v0.9.1 package-identity changes; produces an UNSIGNED APK."""
import struct
OLD, NEW = 'com.follow.clash', 'com.xigua.netapp'
def chunks(buf, start, end):
    off = start
    while off < end:
        typ, hdr, size = struct.unpack_from('<HHI', buf, off)
        assert size >= hdr >= 8 and off + size <= end
        yield off, typ, hdr, size
        off += size
    assert off == end

changes = []
def patch_manifest(data):
    out = bytearray(data)
    for off, typ, hdr, size in chunks(data, 8, len(data)):
        if typ != 1:
            continue
        count, stylecount, flags, stringstart, stylestart = struct.unpack_from('<IIIII', data, off + 8)
        utf8 = bool(flags & 0x100)
        def readlen(p, wide):
            if wide:
                val = struct.unpack_from('<H', data, p)[0]
                return (((val & 0x7fff) << 16) | struct.unpack_from('<H', data, p + 2)[0], p + 4) if val & 0x8000 else (val, p + 2)
            val = data[p]
            return (((val & 0x7f) << 8) | data[p + 1], p + 2) if val & 0x80 else (val, p + 1)
        for i in range(count):
            p = off + stringstart + struct.unpack_from('<I', data, off + hdr + i * 4)[0]
            n, p = readlen(p, not utf8)
            if utf8:
                n, p = readlen(p, False)
            else:
                n *= 2
            encoding = 'utf-8' if utf8 else 'utf-16le'
            value = data[p:p+n].decode(encoding)
            suffixes = ('.permission.', '.action.', '.intent.action.', '.files', '.flutter.', '.firebaseinitprovider', '.mlkitinitprovider', '.androidx-startup', '.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION')
            if value == OLD or any(value.startswith(OLD + s) for s in suffixes):
                value2 = NEW + value[len(OLD):]
                replacement = value2.encode(encoding)
                assert len(replacement) == n
                out[p:p+n] = replacement
                changes.append({'kind': 'manifest', 'old': value, 'new': value2})
    assert len(out) == len(data)
    return bytes(out)

def patch_resources(data):
    out = bytearray(data)
    found = 0
    for off, typ, hdr, size in chunks(data, 12, len(data)):
        if typ != 0x200:
            continue
        p = off + 12
        name = data[p:p+256].decode('utf-16le').split('\0')[0]
        if name == OLD:
            replacement = NEW.encode('utf-16le')
            out[p:p+256] = replacement + bytes(256-len(replacement))
            found += 1
            changes.append({'kind': 'resources package', 'old': OLD, 'new': NEW})
    assert found == 1 and len(out) == len(data)
    return bytes(out)



def main():
    import argparse
    import hashlib
    import pathlib
    import zipfile

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("upstream_apk", type=pathlib.Path)
    parser.add_argument("unsigned_apk", type=pathlib.Path)
    args = parser.parse_args()
    expected = "7a8aeedbe3c376b724a1f76521f5322df1da4bb8d8e09833a2fa804b2913ecc2"
    if hashlib.sha256(args.upstream_apk.read_bytes()).hexdigest() != expected:
        parser.error("Input is not the pinned upstream v0.9.1 arm64 APK.")
    if args.unsigned_apk.exists():
        parser.error("Output already exists; choose a new path.")

    def signature_entry(name):
        upper = name.upper()
        return upper == "META-INF/MANIFEST.MF" or (
            upper.startswith("META-INF/") and upper.endswith((".RSA", ".DSA", ".EC", ".SF"))
        )

    with zipfile.ZipFile(args.upstream_apk) as src, zipfile.ZipFile(args.unsigned_apk, "x") as dst:
        if len(src.namelist()) != len(set(src.namelist())):
            raise ValueError("Duplicate ZIP entries")
        for entry in src.infolist():
            if signature_entry(entry.filename):
                continue
            data = src.read(entry.filename)
            if entry.filename == "AndroidManifest.xml":
                data = patch_manifest(data)
            elif entry.filename == "resources.arsc":
                data = patch_resources(data)
            dst.writestr(entry, data)
    print("Created unsigned APK; align and sign it with your own local key before installation.")


if __name__ == "__main__":
    main()
