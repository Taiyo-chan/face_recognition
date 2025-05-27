import cv2
import face_recognition

# 登録用の顔画像を読み込んで、特徴量を抽出
train_image = face_recognition.load_image_file("train_taiyo.jpg")
train_location = face_recognition.face_locations(train_image)[0]
train_encoding = face_recognition.face_encodings(train_image, [train_location])[0]

# カメラ起動（0は内蔵カメラ）
video = cv2.VideoCapture(0)

print("🎥 カメラ起動。'q' で終了します")

while True:
    ret, frame = video.read()
    if not ret:
        continue

    # OpenCVのフレームをRGBに変換（face_recognition用）
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 顔検出
    face_locations = face_recognition.face_locations(rgb_frame, model="hog")
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # 登録画像との距離を計算
        distance = face_recognition.face_distance([train_encoding], face_encoding)[0]
        print(f"顔の距離: {distance:.2f}")

        # しきい値以下なら一致とみなす
        name = "Unknown"
        if distance < 0.40:
            name = "MATCH"

        # 結果表示
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

    # ウィンドウ表示
    cv2.imshow("リアルタイム顔認識", frame)

    # 'q'で終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
video.release()
cv2.destroyAllWindows()
