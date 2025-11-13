import argparse

def main():
    parser = argparse.ArgumentParser(description="Run retrieval from a config file.")
    parser.add_argument("--config", type=str, required=True, help="Path to config YAML")
    args = parser.parse_args()
    # TODO: load config and call retrieval pipeline
    print(f"[stub] Would run retrieval with config: {args.config}")

if __name__ == "__main__":
    main()
