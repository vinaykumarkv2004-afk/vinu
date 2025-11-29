class VISACard:
    def _init_(self, holder_name, card_number):
        self.holder_name = holder_name
        self.card_number = card_number

    def display_details(self):
        print(self.holder_name)
        print(self.card_number)

    def compute_reward_points(self, purchase_type, amount):
        # 1% reward for all VISA purchases
        reward = amount * 0.01
        return reward


class HPVISACard(VISACard):
    def compute_reward_points(self, purchase_type, amount):
        # 1% reward same as normal VISA
        reward = amount * 0.01

        # Extra 10 reward points if purchase type is exactly "Fuel"
        if purchase_type == "Fuel":
            reward += 10

        return reward


# ------- Main Program --------

card_type = input().strip()
holder_name = input().strip()
card_number = input().strip()
amount = float(input().strip())
purchase_type = input().strip()

# Check card type and create object
if card_type == "VISA":
    card = VISACard(holder_name, card_number)
elif card_type == "HPVISA":
    card = HPVISACard(holder_name, card_number)
else:
    print("Invalid Choice")
    exit()

# Display output
card.display_details()
reward = card.compute_reward_points(purchase_type, amount)
print(f"{reward:.2f}")