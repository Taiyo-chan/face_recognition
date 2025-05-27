import cv2
import face_recognition
import pickle

# 顔データの読み込み
with open("known_faces.pkl", "rb") as f:
    data = pickle.load(f)

# 距離のしきい値（精度の鍵）
THRESHOLD = 0.40  # 0.40 未満なら「一致」と判定

video = cv2.VideoCapture(0)
print("🎥 リアルタイム顔認識開始（'q' で終了）")

while True:
    ret, frame = video.read()
    if not ret:
        continue

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Unknown"
        min_distance = 1.0  # 初期値（最大距離）

        # 全登録顔と距離を計算
        face_distances = face_recognition.face_distance(data["encodings"], face_encoding)

        if len(face_distances) > 0:
            best_match_index = face_distances.argmin()
            min_distance = face_distances[best_match_index]

            if min_distance < THRESHOLD:
                name = data["names"][best_match_index]

        # デバッグ：距離の表示
        print(f"最小距離: {min_distance:.3f} → 判定: {name}")

        # 結果描画
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("1:N 顔認識", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
