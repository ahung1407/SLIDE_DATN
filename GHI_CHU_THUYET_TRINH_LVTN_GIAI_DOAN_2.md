# KỊCH BẢN & GHI CHÚ THUYẾT TRÌNH BẢO VỆ LUẬN VĂN TỐT NGHIỆP
## Đề tài: Hệ thống ghi chỉ số nước thông minh dựa trên NB-IoT và AI OCR
**GVHD**: TS. Lê Trọng Nhân | **Hội đồng**: 4L Kỹ thuật Máy tính  
**SVTH**: Nguyễn Minh Hưng (2211367) – Lê Quang Trưng (2213730) – Nguyễn Văn Huynh (2211315)  
**Thời lượng**: 25 – 30 phút (27 slides)

---

### PHẦN MỞ ĐẦU (Chung cả nhóm)
- **Slide 1 - Bìa đề tài**: Chào Thầy/Cô Hội đồng, giới thiệu tên đề tài và 3 thành viên thực hiện.
- **Slide 2 - Đặt vấn đề & Mục tiêu nghiên cứu**: Nêu thực trạng thất thoát nước sạch (NRW ~20%), hầm ngầm không điện lưới, khó khăn khi thay đồng hồ điện tử đắt tiền ($150-$200). Mục tiêu là giải pháp Retrofit tự chủ năng lượng.
- **Slide 3 - So sánh & Biện luận giải pháp**: Phân tích 3 phương án (Đồng hồ điện tử vs Cảm biến xung vs Retrofit). Nhấn mạnh ưu thế giải pháp của nhóm: chi phí tối ưu ~$35, không cắt ống nước, lưu ảnh gốc 100% minh chứng pháp lý, tự sạc từ dòng chảy.
- **Slide 4 - Kiến trúc tổng thể 4 phân tầng**: Trình bày luồng End-to-End: Thiết bị biên ESP32-S3 -> Mạng NB-IoT -> Cloud Spring Boot -> Dashboard Web/App.

---

### PHẦN 1: THIẾT BỊ BIÊN ESP32 & QUẢN LÝ NĂNG LƯỢNG (Sinh viên 1)
- **Slide 5 - Thiết kế phần cứng Node biên**: Sử dụng vi điều khiển XIAO ESP32-S3 (8MB PSRAM), camera OV2640, module SIM7020G NB-IoT (PSM 3.5µA), RTC DS3231 và mạch sạc bảo vệ pin Li-ion 3000mAh.
- **Slide 6 - Phân hệ thu thập năng lượng (Harvester)**: Tua-bin F50-12V biến đổi động năng dòng nước thành điện; mạch Buck MP2307 hiệu suất >90% hạ áp 5V nạp pin; dòng sạc đạt 112mA tại 10L/phút; chỉ cần 25L nước sinh hoạt/ngày là đủ bù năng lượng.
- **Slide 7 - Firmware FreeRTOS & Tiết kiệm năng lượng**: Phân chia task 2 lõi, FSM Deep-Sleep ngủ 99.8% thời gian, dòng tĩnh chỉ **185 µA**, ngắt nguồn toàn bộ ngoại vi qua MOSFET.
- **Slide 8 - Kỹ thuật chụp ảnh & Nén/cắt tĩnh ROI**: Flash LED 50ms chống rung nhòe, giải thuật cắt tĩnh ROI giảm 80% dung lượng ảnh (từ 120KB xuống 18-25KB), tiết kiệm thời gian phát sóng NB-IoT từ 35s xuống 6.2s.
- **Slide 9 - Kết quả đo kiểm phần cứng (Tektronix DSO)**: Minh chứng số liệu thực tế đo bằng dao động ký Tektronix: dòng tĩnh 185µA, chụp ảnh 68mA (450ms), xung đỉnh phát sóng 285.5mA; pin tự duy trì vĩnh viễn.

---

### PHẦN 2: HỆ THỐNG IoT TRUYỀN THÔNG & CLOUD BACKEND (Sinh viên 2)
- **Slide 10 - Hạ tầng mạng NB-IoT & Giao thức MQTT**: Chuẩn LTE Cat-NB2 suy hao cực đại MCL 164dB xuyên sâu hầm nắp gang; MQTT QoS 1 đảm bảo không mất gói tin; giải quyết bài toán băng thông mà LoRaWAN bị giới hạn Duty Cycle 1%.
- **Slide 11 - Giải thuật phân mảnh & Ghép ảnh**: Chia ảnh 20KB thành các chunk 512B kèm Header CRC16-CCITT; cơ chế Selective ARQ chỉ gửi lại mảnh lỗi; tỷ lệ lắp ráp ảnh thành công đạt **99.8%**.
- **Slide 12 - Kiến trúc Cloud Backend Spring Boot**: Microservices hướng sự kiện (Event-Driven), dịch vụ MQTT Ingestion, Redis cache ghép ảnh tốc độ cao, CSDL MySQL và REST API điều phối sang AI OCR Server.
- **Slide 13 - Giao diện Dashboard Web & Mobile**: Dashboard CoreIoT thời gian thực, bản đồ GIS, tính năng đối soát ảnh gốc song song chỉ số AI đọc được; cảnh báo đa kênh Telegram Bot/SMS/Email.
- **Slide 14 - Kết quả đo kiểm mạng truyền thông**: Thử nghiệm hầm bê tông sâu 1.2m nắp gang đặc tại ĐHQG: PDR đạt **92.4%**, độ trễ truyền ảnh **6.8s**, Cloud chịu tải 500 kết nối MQTT đồng thời phản hồi < 120ms.

---

### PHẦN 3: TRÍ TUỆ NHÂN TẠO AI OCR & PHÂN TÍCH DỮ LIỆU (Sinh viên 3)
- **Slide 15 - Pipeline xử lý ảnh trong điều kiện bất lợi**: Xử lý kính mờ hơi nước, bám bụi và lóa đèn Flash trong hầm tối bằng cân bằng sáng cục bộ CLAHE và lọc song phương Bilateral Filter giữ nét cạnh số.
- **Slide 16 - Thiết kế kiến trúc mô hình AI OCR**: Mạng nơ-ron CRNN (CNN + BiLSTM + CTC) huấn luyện trên 15,000 ảnh thực tế; lượng tử hóa INT8 chỉ nặng 14.2MB, suy luận cực nhanh **142 ms/ảnh**.
- **Slide 17 - Thách thức bánh răng lơ lửng (Rolling Digits)**: Giải thuật Sub-digit Regression nhận diện 2 nửa số đang nhảy kết hợp kiểm tra tính đơn điệu từ cảm biến lưu lượng, tăng độ chính xác từ 61% lên **97.5%**.
- **Slide 18 - Giải thuật phát hiện rò rỉ & Dị thường**: Phân tích chuỗi thời gian, phát hiện rò rỉ ngầm qua lưu lượng đáy ban đêm (> 0.1 L/min trong 3 ngày), cảnh báo vỡ ống (> 45 L/min) và phát hiện dòng chảy ngược.
- **Slide 19 - Kết quả đo kiểm mô hình AI**: Đánh giá 3 bộ dữ liệu: Lý tưởng 99.6%, Mờ hơi nước 98.2%, Bánh răng lơ lửng 97.5%; F1-Score tổng thể đạt **99.05%**.

---

### PHẦN TỔNG HỢP, ĐỐI SOÁT & KẾT LUẬN (Chung cả nhóm)
- **Slide 20 - Tổng hợp kết quả đo kiểm chuyên môn**: 4 khối kết quả định lượng: Năng lượng (185µA, 285.5mA, 25L/ngày); Mạng NB-IoT (92.4% PDR, 6.8s); AI OCR (F1 99.05%); Độ tin cậy (sai số thể tích < 1.8%, sụt áp < 0.05 MPa).
- **Slide 21 - Nhận diện lợi ích thực tế & Tác động toàn diện**: 4 trụ cột Kinh tế (giảm 85% nhân công, ROI 14 tháng); Môi trường (giảm NRW < 8%, không rác thải pin); Xã hội (minh bạch 100%); Kỹ thuật (Retrofit giữ nguyên ống).
- **Slide 22 - Đối soát nhiệm vụ đề tài đặt ra vs. Kết quả**: Đối soát 8/8 hạng mục cam kết; khẳng định hoàn thành **100% khối lượng nhiệm vụ** (vượt chỉ tiêu > 95% theo Rubric Câu 1 để đạt trọn vẹn điểm tối đa).
- **Slide 23 - Kết luận & Hướng phát triển**: Tổng kết thành công của đề tài; định hướng TinyML tại biên, kiểm định IP68 và NSF/ANSI 61, thử nghiệm diện rộng.
- **Slide 24 - Cảm ơn & Mời đặt câu hỏi phản biện**: Cảm ơn Thầy/Cô và Hội đồng.

---

### PHẦN PHỤ LỤC Q&A (Dự phòng phản biện)
- **Slide 25 - Phụ lục 1: Cân bằng năng lượng & Pin**: Giải trình công thức toán học chứng minh năng lượng nạp từ tua-bin (5.42 mAh/ngày) luôn lớn hơn tiêu thụ (4.86 mAh/ngày), độc lập > 600 ngày khi vắng nhà.
- **Slide 26 - Phụ lục 2: Tiêu chuẩn vệ sinh nước uống**: Nhựa kỹ thuật thực phẩm POM/ABS, đạt định hướng NSF/ANSI 61 & WRAS, sụt áp < 0.05 MPa, chịu áp lực 1.2 MPa.
- **Slide 27 - Phụ lục 3: Bảo mật & Toàn vẹn toàn trình**: Khóa eFuse phần cứng, mã hóa TLS v1.3 / MQTTS, chữ ký HMAC-SHA256 và mã băm SHA-256 đối soát ảnh gốc.
