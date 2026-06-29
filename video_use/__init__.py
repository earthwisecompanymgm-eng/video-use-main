from video_use._compat import validate_runtime

def main():
    ok, issues = validate_runtime()
    if not ok:
        for i in issues:
            print(f"  -\x1b[0m {i}")
        sys.exit(1)
    print("\x1b[0;32mvideo-use ready.\x1b[0m")
