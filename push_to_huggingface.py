from datasets import Dataset, DatasetDict
import json

def main():
    with open('ai-leaks-incidents-public.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    verified_data = [d for d in data if d.get('verified') == True]
    
    dataset_dict = DatasetDict({
        'verified': Dataset.from_list(verified_data),
        'full': Dataset.from_list(data)
    })
    
    dataset_dict.push_to_hub(
        'Ahmed-AdelB/ai-security-incidents-2025-2026',
        private=False,
        commit_message='Release v1.0 — 55 incidents, 12 verified, Jan2025-Apr2026'
    )
    
    print(f"Upload summary:")
    print(f"  verified split: {len(verified_data)} records")
    print(f"  full split: {len(data)} records")

if __name__ == '__main__':
    main()
