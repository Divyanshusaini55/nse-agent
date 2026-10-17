#!/usr/bin/env python3
import sys
from agent import sanitize_and_load_pack

def test_research_pack_loading():
    print("=" * 60)
    print("🔍 RUNNING FORENSIC RESEARCH PACK INTEGRITY TEST")
    print("=" * 60)

    folder = "./research_pack"
    corpus, reports = sanitize_and_load_pack(folder)

    print(f"\n1. Document Count Check:")
    print(f"   Expected: 8 documents")
    print(f"   Found   : {len(reports)} documents")
    assert len(reports) == 8, f"Expected 8 documents, but found {len(reports)}"
    print("   ✓ Document count test PASSED.")

    print(f"\n2. Adversarial Injection Detection Check:")
    injections = [r for r in reports if r["has_injection"]]
    print(f"   Injections detected: {len(injections)}")
    
    assert len(injections) == 1, f"Expected exactly 1 injection, found {len(injections)}"
    flagged_file = injections[0]["filename"]
    print(f"   Flagged file: {flagged_file}")
    assert flagged_file == "multibaggeralerts_2026-08-12.md", (
        f"Expected multibaggeralerts_2026-08-12.md to be flagged, got {flagged_file}"
    )

    injection_text = injections[0]["injection_snippets"][0]
    print(f"   Captured Injection Content: \"{injection_text[:70]}...\"")
    assert "ignore all previous instructions" in injection_text, "Failed to capture injection directive"
    print("   ✓ Adversarial injection detection test PASSED.")

    print(f"\n3. XML Boundary & Security Tag Check:")
    assert f'<document filename="{flagged_file}">' in corpus, "Missing XML start tag"
    assert "[SECURITY WARNING: Suspicious hidden HTML comment" in corpus, "Missing security warning banner"
    assert "</document>" in corpus, "Missing XML closing tag"
    print("   ✓ XML boundary sandboxing test PASSED.")

    print("\n" + "=" * 60)
    print("🎉 ALL FORENSIC INTEGRITY TESTS PASSED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        test_research_pack_loading()
    except Exception as e:
        print(f"\n❌ Test Failed: {e}", file=sys.stderr)
        sys.exit(1)
