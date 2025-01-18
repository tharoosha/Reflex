import json
from typing import Dict, Optional

class UserPreferences:
    def __init__(self):
        self.file_path = r'core/userPreferences/preferences.json'
        self.preferences = []

    def load_preferences(self) -> None:
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            self.preferences = data['user_preferences']

    def save_preferences(self) -> None:
        with open(self.file_path, 'w') as f:
            json.dump({'user_preferences': self.preferences}, f, indent=4)

    def get_product_preferences(self, product: str) -> Optional[Dict]:
        for pref in self.preferences:
            if pref['product'].lower() == product.lower():
                return pref['preferences']
        return None

    def update_product_preferences(self, product: str, preferences: Dict) -> bool:
        for pref in self.preferences:
            if pref['product'].lower() == product.lower():
                pref['preferences'] = preferences
                self.save_preferences()
                return True
        return False

    def add_product_preferences(self, product: str, preferences: Dict) -> None:
        new_pref = {
            'product': product,
            'preferences': preferences
        }
        self.preferences.append(new_pref)
        self.save_preferences()

    def remove_product_preferences(self, product: str) -> bool:
        for i, pref in enumerate(self.preferences):
            if pref['product'].lower() == product.lower():
                self.preferences.pop(i)
                self.save_preferences()
                return True
        return False
