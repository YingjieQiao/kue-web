import pyrebase


def main():
    # use firebase for prototyping
    firebase_config = {
        "apiKey": "AIzaSyBF_J7wH5PNs_T2-C89qvybopm6pid8Dk8",
        "authDomain": "kueapp-722a3.firebaseapp.com",
        "databaseURL": "https://kueapp-722a3.firebaseio.com",
        "projectId": "kueapp-722a3",
        "storageBucket": "kueapp-722a3.appspot.com",
        "messagingSenderId": "12190067463",
        "appId": "1:12190067463:web:832bf28c6b4c075001f3a2",
        "measurementId": "G-CN12N924W5"
    }

    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()

    

    data = open("/Users/yingjieqiao/Desktop/kue-web/backend/assets/kue-menu.csv")
    for line in data.readlines():
        if line[0] == 'D':
            continue
        dish = line.split(',')
        payload = {
            "dish": dish[0],
            "price": float(dish[1]),
            "ETA": float(dish[2]),
            "halal": int(dish[3].strip())
        }
        # print(payload)
        db.child("menu").push(payload)


if __name__ == "__main__":
    main()
