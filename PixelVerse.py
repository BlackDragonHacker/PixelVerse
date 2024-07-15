import requests
import time
import os
from colorama import Fore, Style, init
import json
from datetime import datetime, timedelta, timezone
import argparse
import json
  
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://sexyzbot.pxlvrs.io',
    'priority': 'u=1, i',
    'referer': 'https://sexyzbot.pxlvrs.io/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

def get_user_data(query_data):
    url = 'https://api-clicker.pixelverse.xyz/api/users'
    headers['initdata'] = query_data
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Your Query Is Incorrect")
        return None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None
def get_progress(query_data):
    url = 'https://api-clicker.pixelverse.xyz/api/mining/progress'
    headers['initdata'] = query_data
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        return response.json()
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Your Query Is Incorrect")
        return None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None
        
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')        

def get_pets_data(query_data):
    url = 'https://api-clicker.pixelverse.xyz/api/pets'
    headers['initdata'] = query_data
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 

        return response.json()
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Your Query Is Incorrect")
        return None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None

def claim_balance(query_data):
    url = 'https://api-clicker.pixelverse.xyz/api/mining/claim'
    headers['initdata'] = query_data
    try:
        
        response = requests.post(url, headers=headers)
        response.raise_for_status() 

        return response.json()
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Your Query Is Incorrect")
        return None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None
 
start_time = datetime.now()
def calculate_time_difference(last_buy_time_str):
    last_buy_time = datetime.strptime(last_buy_time_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
  
    current_time = datetime.now(timezone.utc)
    
    time_diff = current_time - last_buy_time
    
    hours, remainder = divmod(time_diff.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"{Fore.MAGENTA+Style.BRIGHT}\rBuy Pet : During{int(hours)} hour {int(minutes)} minute", flush=True)

def animated_loading(duration):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        for frame in frames:
            if time.time() >= end_time:
                break
            print(f"\r{Fore.CYAN+Style.BRIGHT}Wait {remaining_time} second.....        ", end="", flush=True)
            time.sleep(0.25)
def print_welcome_message():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m")
    print("\033[1;96m---------------------------------------\033[0m")
    print("\033[1;93mScript created by: Black Dragon Hacker\033[0m")
    print("\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m")
    print("\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m")
    print("\033[1;96m---------------------------------------\033[0m")
    print("\033[1;38;2;139;69;19;48;2;173;216;230m-----------[PixelVerse Bot]-----------\033[0m")
    print("\033[1;96m---------------------------------------\033[0m")
    
    current_time = datetime.now()
    up_time = current_time - start_time
    days, remainder = divmod(up_time.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

def upgrade_pet_if_needed(query_data, max_level):
    pets_data = get_pets_data(query_data)
    if pets_data:
        for pet in pets_data['data']:
            current_level = pet['userPet']['level']
            if current_level < max_level:
                pet_id = pet['userPet']['id']
            
                upgrade_url = f'https://api-clicker.pixelverse.xyz/api/pets/user-pets/{pet_id}/level-up'
                try:
                    headers['initdata'] = query_data
                    upgrade_response = requests.post(upgrade_url, headers=headers)
                    upgrade_response.raise_for_status()
                 
                    print(f"{Fore.GREEN+Style.BRIGHT}\rUpgrade Pet : {pet['name']} Successfully upgraded to Lv. {current_level + 1}", flush=True)
                except requests.RequestException as e:
                    print(f"{Fore.RED+Style.BRIGHT}\rUpgrade Pet : Pet upgrade failed {pet['name']}: {str(e)}", flush=True)
            print(f"{Fore.GREEN+Style.BRIGHT}\rUpgrade Pet : {pet['name']} it's level {max_level}", flush=True)
                
    else:
        print(f"{Fore.RED+Style.BRIGHT}\rUpgrade Pet : Failed to get pet data",flush=True)

def check_daily_rewards(query_data):
    url = 'https://api-clicker.pixelverse.xyz/api/daily-rewards'
    headers['initdata'] = query_data
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        total_claimed = data['totalClaimed']
        day = data['day']
        reward_amount = data['rewardAmount']
        todays_reward_available = data['todaysRewardAvailable']
        status_claim = "Not Yet Claimed" if todays_reward_available else "Already Claimed"
        print(f"{Fore.MAGENTA+Style.BRIGHT}\rDaily Reward : Day {day} Amount {reward_amount}", flush=True)
        print(f"{Fore.YELLOW+Style.BRIGHT}\r{status_claim}", flush=True)
        print(f"{Fore.GREEN+Style.BRIGHT}\rTotal Claimed: {total_claimed}", flush=True)
        if todays_reward_available:
            print(f"{Fore.MAGENTA+Style.BRIGHT}\rDaily Reward : Claiming...", end="", flush=True)
            claim_daily_reward(query_data)
        return data
    except Exception as e:
        print(f"{Fore.RED+Style.BRIGHT}\rDaily Reward : Error: {e}")
        return None

def claim_daily_reward(query_data):
    url = 'https://api-clicker.pixelverse.xyz/api/daily-rewards/claim'
    headers['initdata'] = query_data
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        day = data['day']
        amount = data['amount']
        print(f"{Fore.MAGENTA+Style.BRIGHT}\rDaily Reward : Claimed Day {day} Amount: {amount}", flush=True)
        return data
    except Exception as e:
        print(f"{Fore.RED+Style.BRIGHT}\rDaily Reward : Error: {e}", flush=True)
        return None

def claim_daily_combo(query_data,user_input_order):
    try:
        headers['initdata'] = query_data
        response = requests.get(url="https://api-clicker.pixelverse.xyz/api/cypher-games/current", headers=headers)
        if response.status_code == 200:
            data = response.json()
            combo_id = data.get('id')
            options = data.get('availableOptions')
            
            json_data = {options[i-1]['id']: user_input_order.index(i) for i in user_input_order}
       
            print(f"{Fore.CYAN+Style.BRIGHT}\rDaily Combo : Answering...", flush=True)
            headers['initdata'] = query_data
            response = requests.post(url=f"https://api-clicker.pixelverse.xyz/api/cypher-games/{combo_id}/answer", json=json_data, headers=headers)

            if response.status_code != 400:
                
                data = response.json()
          
                amount = data.get("rewardAmount")
                percent = data.get("rewardPercent")
                print(f"{Fore.CYAN+Style.BRIGHT}\rDaily Combo : Claimed {amount} | {percent}%", flush=True)

            else:
                response = response.json()

                print(f"{Fore.RED+Style.BRIGHT}\rDaily Combo : Failed to claim {response['message']}", flush=True)
                return None
        else:
            response = response.json()
            if "BadRequestException" in response['code']:
                print(f"{Fore.RED+Style.BRIGHT}\rDaily Combo : Daily Combo Already Claimed", flush=True)
            else:
                print(f"{Fore.RED+Style.BRIGHT}\rDaily Combo : Failed to get data", flush=True)
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None 

def main():
    auto_upgrade_pet = input("Auto Upgrade All Pet? (y/n): ").strip().lower()
    if auto_upgrade_pet in ['y', 'n', '']:
        auto_upgrade_pet = auto_upgrade_pet or 'n'
    else:
        print("Insert 'y' or 'n'.")
    if auto_upgrade_pet == 'y':
        max_level_pet = int(input("Enter the maximum level increase (default 10 ) : "))
        if max_level_pet in ['']:
            max_level_pet = 10
    auto_daily_combo = input("Auto Daily Combo? (y/n): ").strip().lower()
    if auto_daily_combo in ['y', 'n', '']:
        auto_daily_combo = auto_daily_combo or 'n'
    else:
        print("Insert 'y' or 'n'.")
    if auto_daily_combo == 'y':
        user_input = input("Enter the Daily Combo sequence (eg: 1,4,3,2): ")
        user_input_order = [int(x.strip()) for x in user_input.split(',')]

    while True:
        print_welcome_message()
        
        try:

            try:
                with open('data.txt', 'r') as file:
                    queries = file.readlines()
                
                for query_data in queries:
                    query_data = query_data.strip()
                    user_response = get_user_data(query_data)
                    
                    if user_response:
                        username = user_response.get('username', "There's no username")
                        clicks_count = "{:,.0f}".format(user_response.get('clicksCount', 0)).replace(',', '.')
                        pet = user_response.get('pet', {})
                        level_up_price = "{:,.0f}".format(pet.get('levelUpPrice', 0)).replace(',', '.')
                        pet_details = f"Level: {pet.get('level', 'N/A')} | Energy: {pet.get('energy', 'N/A')} | Lv. Up Price: {level_up_price}"
                        print(f"{Fore.CYAN+Style.BRIGHT}\n------{username}------")
                        print(f"{Fore.LIGHTYELLOW_EX+Style.BRIGHT}Balance : {clicks_count}")
                        print(f"{Fore.MAGENTA+Style.BRIGHT}Active Pet : {pet_details}")
                        print(f"{Fore.YELLOW+Style.BRIGHT}\rPets : Getting pet data...", end="", flush=True)
                        pets_data = get_pets_data(query_data)
                        if pets_data:
                            try:
                                for pet in pets_data['data']:
                                    pet_level = pet['userPet']['level']
                                    print(f"{Fore.YELLOW+Style.BRIGHT}\rPets : {pet['name']} | Lv. {pet_level}", flush=True)

                            except KeyError as e:
                                print(f"{Fore.RED+Style.BRIGHT}\r[ Pets ] : There is an error: {str(e)}", flush=True)
                        else:
                            print(f"{Fore.RED+Style.BRIGHT}\r[ Pets ] : Failed to get pet data          ",  flush=True)
                        if auto_upgrade_pet == 'y':
                            print(f"{Fore.YELLOW+Style.BRIGHT}\rUpgrade Pet : Upgrading Pet...", end="", flush=True)
                            upgrade_pet_if_needed(query_data, max_level=max_level_pet)
                               
                        check_progress = get_progress(query_data)
                        if check_progress:
                            data = check_progress     
                            max_coin = "{:,.0f}".format(data['maxAvailable']).replace(',', '.')
                            can_claim = "{:,.0f}".format(data['currentlyAvailable']).replace(',', '.')
                            min_claim = "{:,.0f}".format(data['minAmountForClaim']).replace(',', '.')
                            full_claim = datetime.strptime(data['nextFullRestorationDate'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%H hour %M minute")
                            restore_speed = data['restorationPeriodMs']
                            print(f"{Fore.LIGHTYELLOW_EX + Style.BRIGHT}\rClaim : Claiming...")
                            print(f"{Fore.GREEN+Style.BRIGHT}Progress : Can Claim: {can_claim} | Full Claim: {full_claim}")
                            print(f"{Fore.MAGENTA+Style.BRIGHT}Progress : Restore Speed: {restore_speed}")
                            print(f"{Fore.YELLOW+Style.BRIGHT}\rClaim : Claiming...", end="", flush=True)
                            claim = claim_balance(query_data)
                            if claim:
                                claimed_amount = claim.get('claimedAmount', 0)
                                amount = "{:,.0f}".format(claimed_amount).replace(',', '.')
                                print(f"{Fore.GREEN+Style.BRIGHT}\rClaim : Claimed {amount}     ", flush=True)
                            else:
                                if 'message' in claim and claim['message'] == "Claim not available for this user yet":
                                    print(f"{Fore.RED+Style.BRIGHT}\rClaim : It's not time to claim yet", flush=True)
                                else:
                                    print(f"{Fore.RED+Style.BRIGHT}\rClaim : Failed {claim}", flush=True)
                        else:
                            print(f"{Fore.RED + Style.BRIGHT}Progress : Failed to Check Progress {check_progress}")
                        print(Fore.MAGENTA + Style.BRIGHT + f"\rDaily Reward : Checking...", end="", flush=True)   
                        check_daily_rewards(query_data)
                        if auto_daily_combo == 'y':
                            print(Fore.CYAN + Style.BRIGHT + f"\rDaily Combo : Checking...", end="", flush=True)
                            claim_daily_combo(query_data, user_input_order)
                    else:
                        print(f"{Fore.RED + Style.BRIGHT}[\nWrong Query")
                          
                animated_loading(3600)
                clear_terminal()            
            except Exception as e:
                print(f"There is an error: {str(e)}")
        except Exception as e:
            print(f"Error : {str(e)}")

if __name__ == "__main__":
    main()
