import sys
from generator import stream_brochure

if __name__ == "__main__":
    print("---------------------------------------")
    print("   AI Company Brochure Generator  ")
    print("---------------------------------------")

    # Prompt the user for input
    company_name = input("Enter the Company Name: ").strip()
    url = input("Enter the Website URL (including https://): ").strip()

    # Basic Validation
    if not company_name or not url:
        print("\n❌ Error: You must provide both a company name and a URL.")
        sys.exit(1)

    if not url.startswith("http"):
        print("\n⚠️  Warning: Your URL doesn't start with 'http'. The scraper might fail.")
        confirm = input("Do you want to continue anyway? (y/n): ")
        if confirm.lower() != 'y':
            sys.exit(0)

    # Run the brochure generator
    print(f"\nProcessing {company_name}...")
    stream_brochure(company_name, url)