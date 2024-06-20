def solution(record):
    user_info = {}
    actions = []

    for entry in record:
        parts = entry.split()
        action = parts[0]
        user_id = parts[1]
        
        if action in ("Enter", "Change"):
            nickname = parts[2]
            user_info[user_id] = nickname
        
        if action != "Change":
            actions.append((action, user_id))

    result = []
    for action, user_id in actions:
        nickname = user_info[user_id]
        if action == "Enter":
            result.append(f"{nickname}님이 들어왔습니다.")
        elif action == "Leave":
            result.append(f"{nickname}님이 나갔습니다.")
    
    return result

