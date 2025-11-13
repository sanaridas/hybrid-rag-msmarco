import argparse

def main():
    parser = argparse.ArgumentParser(description="Run evaluation from a config file.")
    parser.add_argument("--config", type=str, required=True, help="Path to eval config YAML")
    args = parser.parse_args()
    # TODO: load config and run evaluation
    print(f"[stub] Would run evaluation with config: {args.config}")

if __name__ == "__main__":
    main()
