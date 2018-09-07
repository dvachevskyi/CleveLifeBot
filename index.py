# Да, гавно код, писался на скорую руку
import requests
import json

from vkauth import *



print("\nClever Life Bot v1.01 by dvachevskyi\n### https://github.com/dvachevskyi/CleveLifeBot ###\n\n\n\n")
main_acc  = input('Enter the data from the main account look as login:password without 2FA enabled: ').split(':')
acc = input('Enter the data from the twink account: ').split(':')

def default_headers() -> dict:
    return {
        "User-Agent": "Клевер/2.1.2 (Samsung SM-G935F; Android 22; Scale/1.19; VK SDK 1.6.8; com.vk.quiz)"
    }

def sendInvite():
	main_vk = VKAuth(['1073741823'], '2890984', '5.52', main_acc[0], main_acc[1])
	main_vk.auth()
	main_vk_token = main_vk.get_token()
	main_user_id = main_vk.get_user_id()
	
	twink_vk = VKAuth(['1073741823'], '2890984', '5.52', acc[0], acc[1])
	twink_vk.auth()
	twink_vk_token = twink_vk.get_token()
	twink_user_id = twink_vk.get_user_id()

	# отправка заявки from main to twink
	try:
		response = requests.get('https://api.vk.com/method/friends.add?user_id=' + twink_user_id + '&v=5.84&access_token=' + main_vk_token).json()
		if response["response"] == 1:
			print("Friend request is sent!")
			pass
		else:
			print("[SR] Error!")
			print(response)
			input()
			pass
	except requests.exceptions.ConnectionError:
		print('Connection Error')
		input()

	# принятие заявки в друзья
	try:
		response = requests.get('https://api.vk.com/method/friends.add?user_id=' + main_user_id + '&v=5.84&access_token=' + twink_vk_token).json()
		if response["response"] == 2:
			print("Friend request is accepted!")
			pass
		else:
			print("[AR] Error!")
			print(response)
			input()
			pass
	except requests.exceptions.ConnectionError:
		print('Connection Error')
		input()

	main_kk = VKAuth(['589842'], '6334949', '5.52', main_acc[0], main_acc[1])
	main_kk.auth()
	main_kk = main_kk.get_token()
	
	twink_kk = VKAuth(['589842'], '6334949', '5.52', acc[0], acc[1])
	twink_kk.auth()
	twink_kk_token = twink_kk.get_token()

	try:
		response = requests.get('https://api.vk.com/method/streamQuiz.sendInvites?access_token=' + main_kk + '&user_ids=' + twink_user_id + '&v=5.71&lang=en').json()
		if response["response"]["invites_sent"] == 1:
			print("Invite was sent!")
			pass
		else:
			print("[SI] Error!")
			print(response)
			input()
			pass
	except requests.exceptions.ConnectionError:
		print('Connection Error')
		input()

	# удаление из друзей
	try:
		response = requests.get('https://api.vk.com/method/friends.delete?user_id=' + twink_user_id + '&v=5.84&access_token=' + main_vk_token).json()
		if response["response"]["success"] == 1:
			print("Friend is deleted!")
			pass
		else:
			print("[DF] Error!")
			print(response)
			input()
			pass
	except requests.exceptions.ConnectionError:
		print('Connection Error')
		input()

	# Емуляция входа в клевер
	try:
		response = requests.post("https://api.vk.com/method/execute.getFriendsAvatars", data={"access_token": twink_kk_token, "v": "5.73", "lang": "ru", "https": 1}).text
		if "userapi" in response:
			print("execute.getFriendsAvatars | Success")
			pass
		else:
			print("execute.getFriendsAvatars | Error")
			print(response)
			input()
			pass
	except requests.exceptions.ConnectionError:
		print('Connection Error')
		input()
	try:
		response = requests.post("https://api.vk.com/method/execute.getStartData", data={"access_token": twink_kk_token, "v": "5.73", "lang": "ru", "https": 1, "build_ver": "421001", "func_v": "4", "need_leaderboard": 1}).text
		if "balance" in response:	
			print("execute.getStartData | Success")
			pass
		else:
			print("execute.getStartData | Error")
			print(response)
			input()
			pass
	except requests.exceptions.ConnectionError:
		print('Connection Error')
		input()
	pass

sendInvite();
