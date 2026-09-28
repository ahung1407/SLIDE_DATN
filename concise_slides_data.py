# -*- coding: utf-8 -*-
"""
Dữ liệu 27 slide bảo vệ Luận Văn Tốt Nghiệp Ngành Kỹ Thuật Máy Tính (Giai đoạn 2)
Tối ưu hóa 100% cho Canva Import:
- BỎ hoàn toàn số slide (không đánh số)
- BỎ các chữ nhỏ/nhãn Rubric phía trên tiêu đề
- BẢNG BIỂU ĐƯỢC CHUYỂN THÀNH CARD/CỘT TRỰC QUAN (Canva không bao giờ bị lỗi import table)
- Nội dung cô đọng, chữ to rõ (Tiêu đề 38pt, nội dung 25pt)
- Phân chia 3 phần chuyên môn rành mạch cho 3 sinh viên
"""

SLIDES = [
    # -------------------------------------------------------------
    # SLIDE 1: BÌA ĐỀ TÀI (FORMAT NGUYÊN BẢN GĐ1 - KHÔNG SỐ SLIDE)
    # -------------------------------------------------------------
    {
        "type": "title",
        "topic": "HỆ THỐNG GHI CHỈ SỐ NƯỚC THÔNG MINH\nDỰA TRÊN NB-IoT VÀ AI OCR",
        "sub_topic": "BÁO CÁO ĐỒ ÁN TỐT NGHIỆP NGÀNH KỸ THUẬT MÁY TÍNH",
        "advisor": "GVHD: TS. Lê Trọng Nhân",
        "council": "HỘI ĐỒNG: 4L Kỹ thuật Máy tính",
        "students": [
            "Nguyễn Minh Hưng - 2211367",
            "Lê Quang Trưng - 2213730",
            "Nguyễn Văn Huynh - 2211315"
        ]
    },

    # -------------------------------------------------------------
    # SLIDE 2: ĐẶT VẤN ĐỀ & MỤC TIÊU ĐỀ TÀI
    # -------------------------------------------------------------
    {
        "type": "two_column",
        "title": "Đặt Vấn Đề & Mục Tiêu Nghiên Cứu",
        "left_card": {
            "title": "Thực Trạng & Thách Thức Kỹ Thuật",
            "bullets": [
                [("• ", False), ("Thất thoát nước sạch (NRW): ", True), ("Chiếm tới ", False), ("18% - 22%", True), (" sản lượng do không phát hiện rò rỉ ngầm kịp thời.")],
                [("• ", False), ("Ghi số thủ công: ", True), ("Tốn kém nhân lực, chu kỳ theo tháng, sai sót con người và ", False), ("thiếu ảnh đối soát minh bạch", True), (".")],
                [("• ", False), ("Hầm ngầm khắc nghiệt: ", True), ("Đồng hồ đặt dưới hầm sâu, nắp gang dày, ẩm ướt và ", False), ("hoàn toàn không có điện lưới", True), (".")],
                [("• ", False), ("Đồng hồ điện tử đắt đỏ: ", True), ("Chi phí đầu tư quá lớn ($150 - $200), phải cắt đường ống nước hàng loạt.")],
            ]
        },
        "right_box": {
            "fig_title": "Giải Pháp Thiết Bị Retrofit Thông Minh",
            "points": [
                "Module Retrofit gắn ngoài: Lắp trực tiếp lên đồng hồ cơ cũ, không cần cắt ống nước.",
                "Tự chủ năng lượng: Tua-bin thủy lực mini tự phát điện từ dòng nước sạc cho pin Li-ion.",
                "Truyền dẫn NB-IoT: Xuyên hầm sâu nắp gang, gửi ảnh ROI và lưu lượng lên Cloud.",
                "AI OCR & Dashboard: Tự động đọc chỉ số, phát hiện rò rỉ và đối soát minh bạch."
            ],
            "hint": "(Gợi ý: Chèn ảnh thực tế đồng hồ nước cơ hiện hữu và mô hình thiết bị Retrofit)"
        }
    },

    # -------------------------------------------------------------
    # SLIDE 3: MA TRẬN SO SÁNH & BIỆN LUẬN GIẢI PHÁP (3 CỘT TRỰC QUAN - THAY THẾ BẢNG)
    # -------------------------------------------------------------
    {
        "type": "three_column_compare",
        "title": "So Sánh & Biện Luận Lựa Chọn Giải Pháp",
        "columns": [
            {
                "title": "Đồng Hồ Điện Tử Mới",
                "is_highlight": False,
                "badge": "Chi Phí Cao",
                "items": [
                    ("Chi phí đầu tư:", "Rất cao ($150 - $200/node)"),
                    ("Thi công:", "Cắt ống, gián đoạn cấp nước"),
                    ("Bằng chứng pháp lý:", "Không có ảnh lưu vết"),
                    ("Nguồn năng lượng:", "Pin đóng gói, hết pin thay cả cụm"),
                    ("Đánh giá:", "Không khả thi triển khai đại trà")
                ]
            },
            {
                "title": "Cảm Biến Xung (Reed Switch)",
                "is_highlight": False,
                "badge": "Sai Số Tích Lũy",
                "items": [
                    ("Chi phí đầu tư:", "Thấp ($10 - $15/node)"),
                    ("Thi công:", "Khoan mặt kính hoặc gắn keo"),
                    ("Bằng chứng pháp lý:", "Không có ảnh đối soát khiếu nại"),
                    ("Sai số đo đếm:", "Sai số cộng dồn vĩnh viễn theo thời gian"),
                    ("Đánh giá:", "Dễ lỗi đếm xung, tranh chấp hóa đơn")
                ]
            },
            {
                "title": "Retrofit Camera + Tua-Bin AI",
                "is_highlight": True,
                "badge": "★ GIẢI PHÁP LỰA CHỌN",
                "items": [
                    ("Chi phí đầu tư:", "Tối ưu (~$35/thiết bị)"),
                    ("Thi công:", "Gắn ngoài (Non-invasive), giữ nguyên ống"),
                    ("Bằng chứng pháp lý:", "Lưu ảnh gốc đối soát 100%"),
                    ("Nguồn năng lượng:", "Tua-bin tự sạc từ dòng chảy nước"),
                    ("Đánh giá:", "Tự chủ năng lượng, minh bạch, chi phí thấp")
                ]
            }
        ]
    },

    # -------------------------------------------------------------
    # SLIDE 4: KIẾN TRÚC TỔNG THỂ HỆ THỐNG 4 PHÂN TẦNG
    # -------------------------------------------------------------
    {
        "type": "two_column",
        "title": "Kiến Trúc Tổng Thể Hệ Thống 4 Phân Tầng",
        "left_card": {
            "title": "4 Phân Tầng Hệ Thống (End-to-End)",
            "bullets": [
                [("1. Tầng Thiết bị Biên: ", True), ("XIAO ESP32-S3 Sense, Camera OV2640, SIM7020G, Tua-bin F50, Pin Li-ion 3000mAh. Đo lưu lượng, chụp ảnh và cắt ROI.")],
                [("2. Tầng Mạng Truyền dẫn: ", True), ("Mạng di động ", False), ("NB-IoT (Băng tần B3/B8/B20)", True), (", giao thức MQTT/TLS bảo mật kênh truyền.")],
                [("3. Tầng Dịch vụ Đám mây: ", True), ("Spring Boot Microservices, EMQX Broker, MySQL, Redis cache và AI Dispatcher điều phối xử lý.")],
                [("4. Tầng Ứng dụng: ", True), ("Web CoreIoT & Mobile App giám sát lưu lượng thời gian thực, quản lý khách hàng và xuất hóa đơn.")],
            ]
        },
        "right_box": {
            "fig_title": "Sơ Đồ Luồng Dữ Liệu 4 Phân Tầng",
            "points": [
                "Luồng Thu thập: Đồng hồ cơ -> Tua-bin phát điện + ESP32-S3 chụp ảnh ROI.",
                "Luồng Truyền tin: Node biên phân mảnh 512B -> Mạng NB-IoT -> EMQX Broker.",
                "Luồng Xử lý: Cloud Backend ghép ảnh -> Gọi AI OCR Microservice bóc tách số.",
                "Luồng Giám sát: Lưu MySQL -> Đẩy Dashboard Web/App & Cảnh báo rò rỉ tự động."
            ],
            "hint": "(Gợi ý: Chèn sơ đồ kiến trúc tổng thể 4 phân tầng của hệ thống từ Báo cáo)"
        }
    },

    # =============================================================
    # PHẦN 1: THIẾT BỊ BIÊN ESP32 & QUẢN LÝ NĂNG LƯỢNG (SINH VIÊN 1)
    # =============================================================
    {
        "type": "two_column",
        "title": "Thiết Kế Phần Cứng Node Biên & Cảm Biến",
        "left_card": {
            "title": "Cấu Trúc Phần Cứng Node Đo Đếm",
            "bullets": [
                [("• ", False), ("Bộ xử lý trung tâm: ", True), ("Seeed Studio XIAO ESP32-S3 Sense (Dual-core 240MHz, ", False), ("8MB PSRAM, 8MB Flash", True), (") đủ bộ nhớ đệm xử lý ảnh.")],
                [("• ", False), ("Camera & Chiếu sáng: ", True), ("OV2640 2 Megapixel góc hẹp, tích hợp Flash LED xung ngắn ", False), ("50ms", True), (" chống nhòe và chói lóa trong hầm tối.")],
                [("• ", False), ("Module Truyền thông: ", True), ("SIM7020G NB-IoT, giao tiếp UART, dòng tiêu thụ chế độ PSM chỉ ", False), ("3.5 µA", True), (".")],
                [("• ", False), ("Đồng hồ RTC & Cảm biến: ", True), ("RTC DS3231 độ chính xác cao đánh thức định kỳ; cảm biến dòng chảy YF-S201 giám sát lưu lượng.")],
            ]
        },
        "right_box": {
            "fig_title": "Sơ Đồ Khối Phần Cứng Node Biên",
            "points": [
                "Khối Vi điều khiển: XIAO ESP32-S3 kết nối DVP Camera OV2640.",
                "Khối Truyền thông: SIM7020G kết nối UART TX/RX + chân PWRKEY kích hoạt nguồn.",
                "Khối RTC & Đánh thức: DS3231 kết nối I2C + ngắt INT nối chân GPIO đánh thức ngoài.",
                "Thiết kế mạch in (PCB) 2 lớp: Tối ưu đường mass GND, bọc chống nhiễu RF cho SIM."
            ],
            "hint": "(Gợi ý: Chèn sơ đồ nguyên lý phần cứng hoặc hình ảnh mạch PCB thực tế)"
        }
    },

    {
        "type": "two_column",
        "title": "Phân Hệ Thu Thập Năng Lượng Thủy Lực (Harvester)",
        "left_card": {
            "title": "Thu Hoạch Năng Lượng Từ Dòng Chảy Nước",
            "bullets": [
                [("• ", False), ("Máy phát thủy điện Mini: ", True), ("Model F50-12V biến đổi động năng dòng nước chảy qua đường ống thành điện áp AC.")],
                [("• ", False), ("Chỉnh lưu & Hạ áp Buck: ", True), ("Chỉnh lưu cầu Schottky (sụt áp thấp 0.3V) kết hợp mạch Buck ", False), ("MP2307 hiệu suất > 90%", True), (" hạ áp ổn định 5V sạc pin.")],
                [("• ", False), ("Bảo vệ Pin Li-ion: ", True), ("Pin 18650 3.7V 3000mAh tích hợp IC sạc TP4056 và IC bảo vệ quá sạc/quá xả DW01A + FS8205A.")],
                [("• ", False), ("Khả năng tự duy trì: ", True), ("Tự khởi động sạc tại ", False), ("Q ≥ 2.5 L/phút", True), ("; dòng nạp đạt ", False), ("112 mA", True), (" tại lưu lượng 10 L/phút.")],
            ]
        },
        "right_box": {
            "fig_title": "Đặc Tuyến Sạc Tua-Bin Theo Lưu Lượng Nước",
            "points": [
                "Lưu lượng khởi động sạc (Cut-in Flow): 2.5 Lít/phút (Điện áp hở mạch 4.2V).",
                "Lưu lượng vòi nước sinh hoạt (5 - 8 L/phút): Dòng nạp 45 - 85 mA.",
                "Lưu lượng cực đại (10 Lít/phút): Dòng sạc đạt đỉnh 112 mA (Công suất ~0.56W).",
                "Kết luận: Mỗi ngày chỉ cần người dùng xả nước sinh hoạt 25 lít là đủ bù năng lượng tiêu thụ cả ngày!"
            ],
            "hint": "(Gợi ý: Chèn đồ thị đặc tuyến sạc Tua-bin F50 hoặc sơ đồ nguyên lý mạch nguồn)"
        }
    },

    {
        "type": "two_column",
        "title": "Thiết Kế Firmware FreeRTOS & Tiết Kiệm Năng Lượng",
        "left_card": {
            "title": "Quản Lý Đa Nhiệm & Chế Độ Ngủ Sâu",
            "bullets": [
                [("• ", False), ("Đa nhiệm FreeRTOS: ", True), ("Phân bổ Core 0 (Task Chụp ảnh & Cắt ROI) và Core 1 (Task Truyền NB-IoT). Hàng đợi Queue truyền con trỏ đệm an toàn.")],
                [("• ", False), ("Chu Trình Deep-Sleep: ", True), ("Thiết bị ở trạng thái ngủ sâu ", False), ("99.8% thời gian", True), (", ngắt toàn bộ nguồn cấp Camera, Flash LED và SIM7020G qua MOSFET.")],
                [("• ", False), ("Dòng tĩnh cực thấp: ", True), ("Dòng tiêu thụ ở chế độ Deep-Sleep chỉ đạt ", False), ("185 µA", True), (" (đo thực tế trên bo mạch hoàn chỉnh).")],
                [("• ", False), ("Đánh thức linh hoạt: ", True), ("Đánh thức định kỳ bởi RTC DS3231 hoặc ngắt ngoài khi phát hiện lưu lượng nước chảy bất thường.")],
            ]
        },
        "right_box": {
            "fig_title": "Máy Trạng Thái FSM Chu Trình Hoạt Động",
            "points": [
                "Trạng thái 1: Deep Sleep (Ngắt toàn bộ ngoại vi, dòng tĩnh 185 µA).",
                "Trạng thái 2: Wake-up do RTC -> Kích hoạt nguồn 3.3V/5V cho Camera & Cảm biến.",
                "Trạng thái 3: Chụp ảnh UXGA -> Cắt tĩnh vùng số ROI (450 ms, 68 mA).",
                "Trạng thái 4: Bật SIM7020G -> Kết nối MQTT -> Truyền mảnh ảnh qua NB-IoT (6.2 s, 120 mA).",
                "Trạng thái 5: Nhận ACK từ Server -> Tắt toàn bộ nguồn ngoại vi -> Quay lại Deep Sleep."
            ],
            "hint": "(Gợi ý: Chèn lưu đồ máy trạng thái FSM hoặc sơ đồ nhiệm vụ FreeRTOS từ Báo cáo)"
        }
    },

    {
        "type": "two_column",
        "title": "Kỹ Thuật Chụp Ảnh & Nén/Cắt Tĩnh ROI Tại Biên",
        "left_card": {
            "title": "Tối Ưu Hóa Kích Thước Dữ Liệu Hình Ảnh",
            "bullets": [
                [("• ", False), ("Thách thức băng thông: ", True), ("Tốc độ tải lên NB-IoT bị giới hạn, không thể truyền ảnh thô độ phân giải cao liên tục mà vẫn tiết kiệm pin.")],
                [("• ", False), ("Chụp ảnh chất lượng cao: ", True), ("Camera OV2640 chụp ảnh JPEG UXGA (1600x1200) bật Flash LED xung ngắn ", False), ("50ms", True), (" loại trừ rung nhòe.")],
                [("• ", False), ("Cắt tĩnh ROI tại biên: ", True), ("Trích xuất chính xác vùng chữ số đồng hồ nước, ", False), ("giảm dung lượng ảnh từ 120 KB xuống còn 18 - 25 KB", True), (".")],
                [("• ", False), ("Tiết kiệm 80% năng lượng RF: ", True), ("Giảm thời gian phát sóng NB-IoT từ 35 giây xuống 6.2 giây, bảo vệ tuổi thọ pin tối đa.")],
            ]
        },
        "right_box": {
            "fig_title": "Minh Họa Vùng Cắt Tĩnh ROI Trên Mặt Đồng Hồ",
            "points": [
                "Ảnh Gốc (Full Frame 1600x1200): Dung lượng ~120 KB (toàn bộ mặt đồng hồ).",
                "Xác định tọa độ ROI cố định: Nhờ ngàm giữ Camera cơ khí cố định khoảng cách và góc nhìn.",
                "Ảnh Cắt ROI (Cropped ROI): Dung lượng ~18 - 25 KB (chỉ chứa hộp 8 chữ số đo nước).",
                "Độ sắc nét: Đảm bảo độ tương phản cao để thuật toán AI OCR nhận diện chính xác 100%."
            ],
            "hint": "(Gợi ý: Chèn ảnh chụp thực tế mặt đồng hồ gốc và ảnh sau khi cắt ROI)"
        }
    },

    {
        "type": "two_column",
        "title": "Kết Quả Đo Kiểm Chuyên Môn Phân Hệ Phần Cứng",
        "left_card": {
            "title": "Đo Dòng Tiêu Thụ Bằng Dao Động Ký (DSO Tektronix)",
            "bullets": [
                [("• ", False), ("Thiết bị đo chuyên dụng: ", True), ("Dao động ký số Tektronix DSO kết hợp điện trở Shunt 1Ω đo dòng tức thời.")],
                [("• ", False), ("Dòng tĩnh chế độ Deep Sleep: ", True), ("Đạt ", False), ("185 µA", True), (" (thấp hơn chỉ tiêu thiết kế ban đầu 250 µA).")],
                [("• ", False), ("Pha Chụp ảnh & Cắt ROI: ", True), ("Dòng trung bình ", False), ("68 mA", True), (" trong thời gian ngắn ", False), ("450 ms", True), (".")],
                [("• ", False), ("Pha Truyền tin NB-IoT: ", True), ("Xung đỉnh ", False), ("285.5 mA", True), (" (trong 150ms đầu kết nối), dòng phát trung bình ", False), ("120 mA", True), (" trong 6.2s.")],
                [("• ", False), ("Đánh giá tự chủ năng lượng: ", True), ("Lưu lượng sinh hoạt 25L/ngày bù đắp 100% điện năng; hoạt động độc lập không sạc ", False), ("> 180 ngày", True), (".")],
            ]
        },
        "right_box": {
            "fig_title": "Dạng Sóng Tiêu Thụ Dòng Đo Bằng Tektronix DSO",
            "points": [
                "Trục ngang: Thời gian thực thi chu trình (s). Trục đứng: Dòng điện tức thời (mA).",
                "Vùng 1: Thức dậy từ Deep Sleep & Ổn định nguồn Camera (t = 0 đến 0.2s, I = 35 mA).",
                "Vùng 2: Bật Flash LED + Chụp ảnh UXGA + Cắt ROI (t = 0.2 đến 0.65s, I = 68 mA).",
                "Vùng 3: Kích hoạt SIM7020G + Bắt sóng trạm BTS NB-IoT (Xung đỉnh I_peak = 285.5 mA).",
                "Vùng 4: Truyền phân mảnh MQTT QoS 1 + Nhận ACK Server (I_avg = 120 mA, duration = 6.2s)."
            ],
            "hint": "(Gợi ý: Chèn ảnh chụp dạng sóng dao động ký Tektronix DSO từ Báo cáo)"
        }
    },

    # =============================================================
    # PHẦN 2: HỆ THỐNG IoT TRUYỀN THÔNG & CLOUD BACKEND (SINH VIÊN 2)
    # =============================================================
    {
        "type": "two_column",
        "title": "Hạ Tầng Mạng NB-IoT & Giao Thức MQTT",
        "left_card": {
            "title": "Lựa Chọn Chuẩn Mạng & Giao Thức Truyền Tin",
            "bullets": [
                [("• ", False), ("Công nghệ NB-IoT (LTE Cat-NB2): ", True), ("Độ nhạy thu vượt trội với ngân sách suy hao đường truyền ", False), ("MCL = 164 dB", True), (" (tốt hơn 20dB so với 2G/GSM).")],
                [("• ", False), ("Khả năng xuyên hầm sâu: ", True), ("Sóng di động băng tần hẹp xuyên sâu qua nắp gang và hầm bê tông, không cần xây dựng Gateway trung gian như LoRaWAN.")],
                [("• ", False), ("Giao thức MQTT qua TCP/IP: ", True), ("Kiến trúc Publish/Subscribe nhẹ, kết nối bảo mật tới EMQX Broker trên Cloud.")],
                [("• ", False), ("Cấu hình tin cậy QoS 1: ", True), ("Đảm bảo bản tin chuyển phát thành công với cơ chế bắt tay PUBACK; hỗ trợ giữ phiên qua CleanSession=0.")],
            ]
        },
        "right_box": {
            "fig_title": "Kiến Trúc Mạng Truyền Thông Từ Hầm Ngầm Tới Cloud",
            "points": [
                "Node Biên (Trong hầm ngầm): SIM7020G gửi các gói tin NB-IoT qua anten chống ẩm.",
                "Trạm phát sóng di động (eNodeB): Thu nhận tín hiệu suy hao cao, chuyển vào mạng lõi EPC.",
                "EMQX MQTT Broker (Cloud): Tiếp nhận luồng Publish dữ liệu lưu lượng và mảnh ảnh.",
                "So sánh LoRaWAN vs NB-IoT: LoRaWAN bị giới hạn Duty Cycle 1% (không đủ truyền ảnh 20KB); NB-IoT đáp ứng hoàn hảo yêu cầu truyền ảnh định kỳ."
            ],
            "hint": "(Gợi ý: Chèn sơ đồ kết nối mạng NB-IoT và luồng dữ liệu MQTT)"
        }
    },

    {
        "type": "two_column",
        "title": "Giải Thuật Phân Mảnh & Ghép Ảnh Đảm Bảo Toàn Vẹn",
        "left_card": {
            "title": "Truyền Ảnh An Toàn Qua Mạng Băng Hẹp",
            "bullets": [
                [("• ", False), ("Ràng buộc gói tin (MTU): ", True), ("Gói tin NB-IoT có kích thước tải hữu ích tối ưu chỉ từ 512 đến 1024 bytes; trong khi ảnh ROI là 18 - 25 KB.")],
                [("• ", False), ("Phân mảnh thích ứng: ", True), ("Ảnh được chia thành N mảnh (512 bytes/mảnh). Mỗi mảnh có Header: ", False), ("Image_ID | Chunk_Idx | Total | CRC16", True), (".")],
                [("• ", False), ("Kiểm tra lỗi toàn vẹn: ", True), ("Sử dụng mã kiểm tra ", False), ("CRC16-CCITT", True), (" phát hiện lỗi bit trên từng mảnh và mã băm SHA-256 đối soát toàn bộ bức ảnh.")],
                [("• ", False), ("Truyền lại thông minh (ARQ): ", True), ("Server chỉ yêu cầu truyền lại đúng các mảnh lỗi/mất; tỷ lệ lắp ráp ảnh thành công đạt ", False), ("99.8%", True), (".")],
            ]
        },
        "right_box": {
            "fig_title": "Lưu Đồ Thuật Toán Phân Mảnh & Cơ Chế Ghép Gói",
            "points": [
                "Bước 1 (Node): Đọc bộ nhớ đệm ảnh JPEG -> Cắt thành các chunk 512B -> Gắn Header & CRC16.",
                "Bước 2 (Node): Publish tuần tự lên Topic: meters/{id}/image/chunk.",
                "Bước 3 (Cloud): Worker tiếp nhận từng mảnh -> Kiểm tra CRC16 -> Lưu vào bộ nhớ đệm tạm.",
                "Bước 4 (Cloud): Khi nhận đủ N mảnh -> Ghép thành file JPEG hoàn chỉnh -> Kiểm tra Header JPEG.",
                "Bước 5 (Cloud): Nếu thiếu mảnh sau timeout -> Gửi bản tin NACK qua MQTT yêu cầu truyền lại."
            ],
            "hint": "(Gợi ý: Chèn lưu đồ thuật toán phân mảnh gói tin và ghép ảnh tại Cloud Backend)"
        }
    },

    {
        "type": "two_column",
        "title": "Kiến Trúc Nền Tảng Cloud Backend Spring Boot & CSDL",
        "left_card": {
            "title": "Kiến Trúc Microservices Hướng Sự Kiện",
            "bullets": [
                [("• ", False), ("Công nghệ nền tảng: ", True), ("Java Spring Boot Microservices, kiến trúc hướng sự kiện (Event-Driven) đảm bảo khả năng chịu tải và mở rộng độc lập.")],
                [("• ", False), ("Dịch vụ Tiếp nhận (Ingestion): ", True), ("Duy trì kết nối bền vững với EMQX Broker, phân loại bản tin Telemetry và Mảnh ảnh.")],
                [("• ", False), ("Dịch vụ Điều phối AI: ", True), ("Khi ghép xong ảnh hợp lệ, đẩy bất đồng bộ sang AI OCR Microservice qua RESTful API.")],
                [("• ", False), ("Cơ sở dữ liệu kết hợp: ", True), ("MySQL lưu trữ quan hệ khách hàng, thiết bị và hóa đơn; ", False), ("Redis Cache", True), (" lưu trạng thái mảnh ảnh và phiên làm việc.")],
            ]
        },
        "right_box": {
            "fig_title": "Sơ Đồ Phân Phối Dịch Vụ Backend & CSDL (ERD)",
            "points": [
                "MQTT Ingestion: Bắt sự kiện bản tin telemetry và mảnh ảnh từ các node đồng hồ.",
                "Image Assembler Worker: Quản lý luồng ghép ảnh song song trong Redis đệm.",
                "AI Dispatcher Client: Gửi ảnh sang Flask AI Server và nhận kết quả JSON số nước.",
                "Business Core & Billing Service: Tính toán lượng nước tiêu thụ trong kỳ và sinh hóa đơn điện tử.",
                "Cơ sở dữ liệu MySQL: Thiết kế bảng rõ ràng (meters, readings, customers, alerts, invoices)."
            ],
            "hint": "(Gợi ý: Chèn sơ đồ kiến trúc Microservices Spring Boot và lược đồ CSDL ERD)"
        }
    },

    {
        "type": "two_column",
        "title": "Giao Diện Dashboard Web & Mobile Giám Sát Thời Gian Thực",
        "left_card": {
            "title": "Tính Năng Dashboard Quản Trị & Đối Soát",
            "bullets": [
                [("• ", False), ("Giao diện Web CoreIoT: ", True), ("Xây dựng trên ReactJS/Tailwind CSS, giao diện tương tác trực quan thời gian thực qua WebSocket.")],
                [("• ", False), ("Đối soát ảnh gốc minh bạch: ", True), ("Hiển thị song song ", False), ("ảnh chụp gốc", True), (" đồng hồ nước bên cạnh ", False), ("chỉ số do AI đọc", True), (", giải quyết dứt điểm khiếu nại khách hàng.")],
                [("• ", False), ("Giám sát sức khỏe thiết bị: ", True), ("Theo dõi điện áp pin Li-ion (V), công suất nạp tua-bin, cường độ sóng RSSI/SNR và lưu lượng tức thời (L/h).")],
                [("• ", False), ("Cảnh báo đa kênh: ", True), ("Tự động phát cảnh báo rò rỉ nước, vỡ ống hoặc tháo gỡ trái phép qua ", False), ("Telegram Bot, SMS và Email", True), (".")],
            ]
        },
        "right_box": {
            "fig_title": "Giao Diện Dashboard Quản Trị & Ứng Dụng Mobile",
            "points": [
                "Màn hình Tổng quan: Bản đồ định vị các trạm đồng hồ nước trên bản đồ GIS.",
                "Màn hình Chi tiết Đồng hồ: Biểu đồ tiêu thụ nước theo giờ/ngày/tháng và trạng thái pin.",
                "Màn hình Đối soát Chỉ số: Bảng liệt kê chỉ số nước kèm ảnh chụp ROI làm bằng chứng.",
                "Cảnh báo tức thời: Thông báo đẩy khi lưu lượng đêm vượt ngưỡng bất thường (Leak Alarm)."
            ],
            "hint": "(Gợi ý: Chèn ảnh chụp màn hình Web Dashboard quản lý và ứng dụng Mobile)"
        }
    },

    {
        "type": "two_column",
        "title": "Kết Quả Đo Kiểm Chuyên Môn Mạng Truyền Thông",
        "left_card": {
            "title": "Thử Nghiệm Mạng NB-IoT Tại Hầm Sâu Thực Tế",
            "bullets": [
                [("• ", False), ("Điều kiện hiện trường: ", True), ("Đồng hồ lắp đặt trong hầm ngầm bê tông sâu 1.2m, đậy nắp gang đặc dày 50mm tại khu đô thị ĐHQG TP.HCM.")],
                [("• ", False), ("Tỷ lệ truyền gói (PDR): ", True), ("Đạt ", False), ("92.4%", True), (" trong điều kiện nắp gang đóng kín (và đạt ", False), ("98.6%", True), (" trong điều kiện nắp composite).")],
                [("• ", False), ("Thời gian truyền ảnh (Latency): ", True), ("Trung bình ", False), ("6.8 giây", True), (" cho file ảnh ROI dung lượng 20 KB (gồm 40 mảnh gói tin).")],
                [("• ", False), ("Khả năng chịu tải Cloud: ", True), ("Xử lý đồng thời ", False), ("500 kết nối MQTT", True), (" gửi dữ liệu, thời gian phản hồi API trung bình ", False), ("< 120 ms", True), (".")],
            ]
        },
        "right_box": {
            "fig_title": "Đồ Thị Phân Bố Độ Trễ & Tỷ Lệ Mất Gói PDR",
            "points": [
                "Độ trễ thiết lập mạng (Attach Network): 2.1s (dùng cơ chế PSM/eDRX giảm còn 0.4s).",
                "Độ trễ truyền tải 40 mảnh ảnh: 4.3s qua mạng NB-IoT Viettel B3/B8.",
                "Độ trễ xử lý ghép ảnh & Lưu CSDL: 0.4s tại Cloud Backend.",
                "Tổng thời gian Node thức dậy truyền tin: ~6.8s (tối ưu tiêu thụ năng lượng)."
            ],
            "hint": "(Gợi ý: Chèn biểu đồ phân bố độ trễ truyền dữ liệu và tỷ lệ mất gói PDR)"
        }
    },

    # =============================================================
    # PHẦN 3: TRÍ TUỆ NHÂN TẠO AI OCR & PHÂN TÍCH DỮ LIỆU (SINH VIÊN 3)
    # =============================================================
    {
        "type": "two_column",
        "title": "Pipeline Xử Lý Ảnh Đồng Hồ Nước Trong Điều Kiện Bất Lợi",
        "left_card": {
            "title": "Tiền Xử Lý Ảnh Chống Nhiễu Môi Trường",
            "bullets": [
                [("• ", False), ("Đặc thù ảnh chụp hầm nước: ", True), ("Mặt kính bị đọng hơi nước mờ đục, bám bụi bẩn, lóa sáng cục bộ từ đèn Flash LED và góc nghiêng.")],
                [("• ", False), ("Thuật toán CLAHE: ", True), ("(Contrast Limited Adaptive Histogram Equalization) phân vùng cục bộ, tăng cường độ tương phản chữ số mà không khuếch đại nhiễu nền.")],
                [("• ", False), ("Lọc song phương (Bilateral Filter): ", True), ("Làm mịn các hạt nước đọng trên mặt kính nhưng ", False), ("bảo toàn nguyên vẹn đường biên sắc nét", True), (" của các nét chữ số.")],
                [("• ", False), ("Nắn phối cảnh (Perspective Transform): ", True), ("Tự động phát hiện 4 góc hộp số và nắn thẳng góc nhìn về chuẩn trực diện (Frontal View).")],
            ]
        },
        "right_box": {
            "fig_title": "Minh Họa Ảnh Qua Các Bước Tiền Xử Lý CLAHE",
            "points": [
                "Bước 1 (Ảnh đầu vào): Bị lóa sáng Flash LED và có hạt sương ngưng tụ trên kính.",
                "Bước 2 (Chuyển Grayscale): Tách kênh độ sáng loại bỏ sai lệch màu sắc môi trường.",
                "Bước 3 (Áp dụng CLAHE): Làm nổi bật tương phản giữa nét chữ số màu đen/đỏ và nền trắng.",
                "Bước 4 (Bilateral Filter): Khử hạt nhiễu hơi nước, làm mịn bề mặt kính.",
                "Bước 5 (Perspective Transform): Cắt và nắn thẳng khung hiển thị 8 chữ số chuẩn hóa."
            ],
            "hint": "(Gợi ý: Chèn ảnh minh họa kết quả qua từng bước tiền xử lý ảnh CLAHE và khử nhiễu)"
        }
    },

    {
        "type": "two_column",
        "title": "Thiết Kế Kiến Trúc Mô Hình AI OCR Nhận Diện Số",
        "left_card": {
            "title": "Kiến Trúc Mạng Nơ-ron Học Sâu",
            "bullets": [
                [("• ", False), ("Mô hình học sâu CRNN: ", True), ("Sử dụng CNN trích xuất đặc trưng không gian (Feature Maps) kết hợp BiLSTM học mối quan hệ chuỗi ký tự.")],
                [("• ", False), ("Tập dữ liệu huấn luyện: ", True), ("Thu thập ", False), ("15,000 mẫu ảnh", True), (" đồng hồ nước tại Việt Nam đa dạng chủng loại (Kent, Zenner, Asahi, v.v.).")],
                [("• ", False), ("Data Augmentation: ", True), ("Làm giàu dữ liệu nhân tạo bằng cách thêm nhiễu giọt nước, làm mờ quang học, thay đổi độ sáng và xoay nghiêng ±15 độ.")],
                [("• ", False), ("Tối ưu hóa mô hình: ", True), ("Lượng tử hóa INT8, dung lượng mô hình chỉ ", False), ("14.2 MB", True), (", thời gian suy luận chỉ ", False), ("142 ms/ảnh", True), (".")],
            ]
        },
        "right_box": {
            "fig_title": "Kiến Trúc Mạng Nơ-ron Nhận Dạng Ký Tự Chuỗi",
            "points": [
                "Lớp 1 (Convolutional Layers): Trích xuất bản đồ đặc trưng đường nét chữ số.",
                "Lớp 2 (Recurrent Layers - BiLSTM): Học mối quan hệ ngữ cảnh chuỗi số từ trái sang phải.",
                "Lớp 3 (Transcription Layer - CTC Loss): Giải mã nhãn ký tự chuỗi chữ số không cần phân đoạn rời.",
                "Đầu ra: Chuỗi số đo nước chính xác (ví dụ: '00142.85' m³)."
            ],
            "hint": "(Gợi ý: Chèn sơ đồ kiến trúc mạng nơ-ron học sâu OCR hoặc biểu đồ luồng suy luận)"
        }
    },

    {
        "type": "two_column",
        "title": "Giải Quyết Thách Thức Bánh Răng Lơ Lửng (Rolling Digits)",
        "left_card": {
            "title": "Xử Lý Bánh Răng Cơ Học Chuyển Số",
            "bullets": [
                [("• ", False), ("Hiện tượng 'Rolling Digits': ", True), ("Khi đồng hồ cơ chuyển số (từ 9 sang 0), bánh răng số bị lơ lửng ở vị trí giữa, khung chỉ hiển thị ", False), ("nửa trên của số này và nửa dưới của số kia", True), (".")],
                [("• ", False), ("Hạn chế của OCR truyền thống: ", True), ("Thường nhận diện nhầm thành số lạ hoặc trả về độ tự tin rất thấp (Confidence < 0.3).")],
                [("• ", False), ("Giải thuật Sub-digit Regression: ", True), ("Phát hiện đồng thời 2 chữ số lọt khung và tính tỷ lệ dịch chuyển thẳng đứng để xác định trạng thái chuyển tiếp.")],
                [("• ", False), ("Kiểm tra tính đơn điệu: ", True), ("Đối chiếu với chỉ số đo từ cảm biến xung dòng chảy và chỉ số lịch sử để suy luận số hợp lý nhất.")],
            ]
        },
        "right_box": {
            "fig_title": "Minh Họa Hiện Tượng Số Lơ Lửng & Giải Thuật Suy Luận",
            "points": [
                "Hình ảnh thực tế: Bánh răng đang xoay giữa số 3 và số 4 (30% số 3, 70% số 4).",
                "Thuật toán Sub-digit: Trả về xác suất P(3)=0.32, P(4)=0.68 kèm offset dịch chuyển.",
                "Quy tắc quyết định: Nếu bánh răng hàng dưới (lít) chưa qua vạch 0 -> Giữ nguyên số trước (3); nếu đã qua vạch 0 -> Nhảy sang số sau (4).",
                "Kết quả: Nâng độ chính xác nhận diện tại thời điểm chuyển số từ 61% lên 97.5%!"
            ],
            "hint": "(Gợi ý: Chèn ảnh minh họa bánh răng lơ lửng Rolling Digits và lưu đồ giải thuật)"
        }
    },

    {
        "type": "two_column",
        "title": "Giải Thuật Phát Hiện Rò Rỉ & Hành Vi Bất Thường",
        "left_card": {
            "title": "Phân Tích Chuỗi Thời Gian Phát Hiện Rò Rỉ",
            "bullets": [
                [("• ", False), ("Phát hiện rò rỉ ngầm (Continuous Flow): ", True), ("Giám sát lưu lượng ban đêm (1h00 - 4h00 sáng). Nếu lưu lượng liên tục ", False), ("> 0.1 Lít/phút", True), (" trong 3 đêm liên tiếp -> Cảnh báo rò rỉ ngầm.")],
                [("• ", False), ("Phát hiện vỡ đường ống (Burst Pipe): ", True), ("Phát hiện lưu lượng tức thời vượt ngưỡng đột biến ", False), ("> 45 Lít/phút", True), (" kéo dài quá 15 phút -> Kích hoạt cảnh báo khẩn cấp.")],
                [("• ", False), ("Phát hiện chảy ngược & Can thiệp: ", True), ("Đối soát hướng quay cánh quạt Tua-bin và kiểm tra cảm biến Hall; phát hiện dòng chảy ngược hoặc lệch pha giữa OCR và cảm biến xung.")],
                [("• ", False), ("Cảnh báo đa kênh tức thời: ", True), ("Tự động gửi cảnh báo về Dashboard và tin nhắn Telegram Bot cho chủ hộ và công ty cấp nước.")],
            ]
        },
        "right_box": {
            "fig_title": "Đồ Thị Mẫu Lưu Lượng Tiêu Thụ & Ngưỡng Rò Rỉ Đêm",
            "points": [
                "Đường cong tiêu thụ chuẩn: Ban ngày có các đỉnh dùng nước (sáng, trưa, tối); ban đêm lưu lượng về xấp xỉ 0.",
                "Đường cong khi có rò rỉ: Xuất hiện 'mức đáy liên tục' (Baseline Flow) ban đêm không về 0.",
                "Cơ chế lọc nhiễu: Tránh báo động giả khi người dùng thức đêm bằng cách yêu cầu thỏa mãn điều kiện liên tiếp 3 ngày.",
                "Hiệu quả: Giúp gia đình và đơn vị cấp nước phát hiện sớm các điểm bể âm tường, tiết kiệm chi phí."
            ],
            "hint": "(Gợi ý: Chèn đồ thị mẫu lưu lượng tiêu thụ nước và kịch bản phát hiện rò rỉ)"
        }
    },

    {
        "type": "two_column",
        "title": "Kết Quả Đo Kiểm Chuyên Môn Mô Hình AI OCR",
        "left_card": {
            "title": "Đánh Giá Độ Chính Xác Trên 3 Bộ Dữ Liệu Thử Nghiệm",
            "bullets": [
                [("• ", False), ("Bộ 1 - Điều kiện lý tưởng: ", True), ("Ảnh khô ráo, đủ sáng -> Độ chính xác đạt ", False), ("99.6%", True), (".")],
                [("• ", False), ("Bộ 2 - Điều kiện khắc nghiệt: ", True), ("Ảnh đọng hơi nước mờ đục và bám bụi -> Độ chính xác đạt ", False), ("98.2%", True), (" (nhờ có tiền xử lý CLAHE).")],
                [("• ", False), ("Bộ 3 - Bánh răng lơ lửng: ", True), ("Chữ số đang nhảy lơ lửng -> Độ chính xác đạt ", False), ("97.5%", True), (" (nhờ thuật toán Sub-digit).")],
                [("• ", False), ("Chỉ số tổng thể: ", True), ("Precision: ", False), ("99.2%", True), (" | Recall: ", False), ("98.9%", True), (" | ", False), ("F1-Score: 99.05%", True), (".")],
                [("• ", False), ("Tốc độ xử lý: ", True), ("Thời gian suy luận trung bình chỉ ", False), ("142 ms / ảnh", True), (" trên máy chủ GPU/CPU tiêu chuẩn.")],
            ]
        },
        "right_box": {
            "fig_title": "Ma Trận Nhầm Lẫn (Confusion Matrix) & Đồ Thị Đánh Giá",
            "points": [
                "Ma trận nhầm lẫn 10 chữ số (0 - 9): Tỷ lệ nhận diện đúng của từng số đều trên 98.8%.",
                "Các cặp số dễ nhầm lẫn nhất (3 - 8, 1 - 7, 0 - 6): Được giải quyết triệt để nhờ lọc cạnh Bilateral.",
                "Độ trễ toàn trình AI Microservice: Nhận ảnh qua REST API -> Tiền xử lý (35ms) -> Suy luận CRNN (142ms) -> Trả về JSON (8ms). Tổng cộng < 190ms.",
                "Độ ổn định: Đạt tỷ lệ hoàn thành 10,000 yêu cầu bóc tách liên tục không xảy ra lỗi crash."
            ],
            "hint": "(Gợi ý: Chèn ảnh Ma trận nhầm lẫn Confusion Matrix hoặc đồ thị Precision-Recall)"
        }
    },

    # =============================================================
    # PHẦN ĐÁNH GIÁ TỔNG THỂ & KẾT LUẬN (CHUNG NHÓM)
    # =============================================================
    {
        "type": "four_grid",
        "title": "Tổng Hợp Kết Quả Đo Kiểm Kỹ Thuật Chuyên Môn",
        "cards": [
            {
                "title": "1. Năng Lượng & Pin (Tektronix DSO)",
                "bullets": [
                    "Dòng Deep Sleep tĩnh: 185 µA (yêu cầu < 250 µA).",
                    "Dòng phát sóng đỉnh: 285.5 mA trong 150 ms.",
                    "Sạc Tua-bin nước: 112 mA tại lưu lượng 10 L/phút.",
                    "Đánh giá: Tự duy trì vĩnh viễn với 25L nước/ngày."
                ]
            },
            {
                "title": "2. Mạng Truyền Dẫn NB-IoT Hầm Sâu",
                "bullets": [
                    "Tỷ lệ phân phát gói (PDR): 92.4% (hầm bê tông sâu 1.2m nắp gang).",
                    "Độ trễ truyền toàn bộ ảnh 20KB: 6.8 giây qua NB-IoT.",
                    "Khả năng chịu tải: 500 kết nối MQTT đồng thời < 120ms.",
                    "Đánh giá: Vượt trội hoàn toàn so với LoRaWAN hầm sâu."
                ]
            },
            {
                "title": "3. Độ Chính Xác Mô Hình AI OCR",
                "bullets": [
                    "Độ chính xác ảnh lý tưởng: 99.6%.",
                    "Độ chính xác ảnh mờ hơi nước: 98.2% (nhờ CLAHE).",
                    "Độ chính xác số lơ lửng: 97.5% (nhờ Sub-digit).",
                    "Chỉ số F1-Score tổng thể: 99.05% (suy luận 142 ms/ảnh)."
                ]
            },
            {
                "title": "4. Độ Tin Cậy Đo Đếm & Cơ Khí",
                "bullets": [
                    "Sai số lưu lượng thể tích: < 1.8% (đối chuẩn Cấp B).",
                    "Độ sụt áp suất đường ống: ΔP < 0.05 MPa (không ảnh hưởng vòi).",
                    "Áp suất thủy tĩnh chịu đựng: 1.2 MPa (12 bar).",
                    "Đánh giá: Đạt yêu cầu kỹ thuật đo lường dân dụng."
                ]
            }
        ]
    },

    {
        "type": "four_grid",
        "title": "Nhận Diện Lợi Ích Thực Tế & Tác Động Toàn Diện",
        "cards": [
            {
                "title": "1. Khía Cạnh Kinh Tế (Economic)",
                "bullets": [
                    "Giảm 85% chi phí nhân công ghi số thủ công hàng tháng.",
                    "Thời gian hoàn vốn đầu tư (ROI) chỉ trong 14 tháng.",
                    "Phát hiện rò rỉ ngầm sớm, tiết kiệm hàng tỷ đồng thất thoát nước sạch cho đơn vị cấp nước."
                ]
            },
            {
                "title": "2. Khía Cạnh Môi Trường (Environmental)",
                "bullets": [
                    "Bảo tồn tài nguyên nước sạch, giảm tỷ lệ thất thoát (NRW) từ ~20% xuống dưới 8%.",
                    "Thu hoạch năng lượng thủy lực tự nhiên, loại bỏ hoàn toàn rác thải pin độc hại ra môi trường hầm ngầm.",
                    "Hỗ trợ quản lý quy hoạch tài nguyên nước thông minh."
                ]
            },
            {
                "title": "3. Khía Cạnh Xã Hội (Social)",
                "bullets": [
                    "Minh bạch hóa đơn tiền nước 100% nhờ có ảnh chụp gốc đối soát công khai.",
                    "Người dân chủ động theo dõi lượng nước tiêu thụ hàng ngày qua ứng dụng di động.",
                    "Cảnh báo tức thời sự cố rò rỉ âm tường, bảo vệ tài sản người dân."
                ]
            },
            {
                "title": "4. Khía Cạnh Kỹ Thuật (Technical)",
                "bullets": [
                    "Giải pháp Retrofit không xâm lấn, tương thích với hàng triệu đồng hồ cơ khí hiện hữu.",
                    "Không cần cắt ống nước, không làm gián đoạn mạng lưới cấp nước đô thị.",
                    "Làm chủ toàn diện chuỗi công nghệ từ Thiết bị Biên -> NB-IoT -> Cloud -> AI OCR."
                ]
            }
        ]
    },

    # -------------------------------------------------------------
    # SLIDE 22: ĐỐI SOÁT NHIỆM VỤ ĐỀ TÀI (2 CỘT GỌN GÀNG - THAY THẾ BẢNG 8 DÒNG)
    # -------------------------------------------------------------
    {
        "type": "two_column_tasks",
        "title": "Đối Soát Nhiệm Vụ Đề Tài Đặt Ra vs. Kết Quả Thực Hiện",
        "col1_title": "Nhóm Nhiệm Vụ Phần Cứng & Mạng Truyền Dẫn",
        "col1_tasks": [
            ("1. Nghiên cứu & Thiết kế module Retrofit", "Ngàm cơ khí camera và khớp nối tua-bin không cắt ống nước.", "100% Đạt"),
            ("2. Mạch phần cứng ESP32 & Nguồn sạc", "XIAO ESP32-S3, sạc tua-bin MP2307, bảo vệ pin Li-ion an toàn.", "100% Đạt"),
            ("3. Firmware FreeRTOS & Tiết kiệm điện", "Đa nhiệm 2 lõi, FSM Deep-Sleep đạt dòng tĩnh cực thấp 185 µA.", "100% Đạt"),
            ("4. Truyền thông NB-IoT & Giao thức MQTT", "SIM7020G, giao thức MQTT QoS 1, phân mảnh ảnh thích ứng 512B.", "100% Đạt")
        ],
        "col2_title": "Nhóm Nhiệm Vụ Cloud Backend & Trí Tuệ Nhân Tạo",
        "col2_tasks": [
            ("5. Nền tảng Cloud Backend & CSDL", "Hệ thống Spring Boot Microservices, EMQX Broker, MySQL, Redis.", "100% Đạt"),
            ("6. Mô hình AI OCR nhận diện chỉ số", "Pipeline CLAHE, mô hình CRNN đạt F1-Score 99.05%, giải thuật Rolling Digits.", "100% Đạt"),
            ("7. Web Dashboard & Cảnh báo tức thời", "Web CoreIoT thời gian thực, lưu ảnh đối soát, bot cảnh báo Telegram.", "100% Đạt"),
            ("8. Đo kiểm chuyên môn & Đánh giá", "Đo kiểm Tektronix DSO, đo PDR hầm sâu 92.4%, phân tích 4 trụ cột MT/KT/XH.", "100% Đạt")
        ],
        "summary": "KẾT LUẬN: ĐÁP ỨNG ĐẦY ĐỦ 100% NHIỆM VỤ ĐỀ TÀI ĐẶT RA (KHỐI LƯỢNG TRÊN 95% - ĐẠT ĐIỂM TỐI ĐA)"
    },

    {
        "type": "two_column",
        "title": "Kết Luận & Hướng Phát Triển Tương Lai",
        "left_card": {
            "title": "Kết Luận Đề Tài",
            "bullets": [
                [("• ", False), ("Hoàn thành toàn diện hệ thống End-to-End: ", True), ("Xây dựng thành công hệ thống đồng hồ nước thông minh từ thiết bị biên, mạng NB-IoT, Cloud Backend đến AI OCR.")],
                [("• ", False), ("Đột phá về tự chủ năng lượng: ", True), ("Tua-bin thủy lực mini kết hợp Deep-Sleep tối ưu giúp thiết bị tự duy trì năng lượng vĩnh viễn dưới hầm sâu.")],
                [("• ", False), ("Khắc phục triệt để hạn chế đồng hồ cơ: ", True), ("Tự động số hóa chỉ số với độ chính xác F1-Score 99.05%, có ảnh gốc đối soát minh bạch 100%.")],
                [("• ", False), ("Giá trị kinh tế - xã hội cao: ", True), ("Chi phí đầu tư thấp (~$35/node), dễ dàng nhân rộng cho hàng triệu đồng hồ nước hiện hữu.")],
            ]
        },
        "right_box": {
            "fig_title": "Định Hướng Phát Triển Ứng Dụng Thực Tiễn",
            "points": [
                "TinyML tại Biên: Chuyển mô hình OCR trực tiếp lên vi điều khiển ESP32-S3 (chỉ gửi chuỗi số text 8 bytes).",
                "Đăng ký Chuẩn Công nghiệp: Hoàn thiện quy trình kiểm định chống nước ngập chuẩn IP68 và tiêu chuẩn NSF/ANSI 61 cho nước uống.",
                "Thử nghiệm diện rộng: Triển khai thử nghiệm 50 - 100 node tại khu đô thị Đại học Quốc gia TP.HCM.",
                "Mở rộng đa dịch vụ: Ứng dụng giải pháp cho đo đếm thông minh đồng hồ khí gas và điện kế cơ khí."
            ],
            "hint": "(Gợi ý: Chèn ảnh mô hình thiết bị hoàn chỉnh hoặc bản đồ triển khai thử nghiệm diện rộng)"
        }
    },

    {
        "type": "qa",
        "title": "Cảm Ơn & Mời Đặt Câu Hỏi Phản Biện"
    },

    # =============================================================
    # PHẦN PHỤ LỤC Q&A (BACKUP TRẢ LỜI PHẢN BIỆN)
    # =============================================================
    {
        "type": "two_column",
        "title": "Phụ Lục 1: Mô Hình Cân Bằng Năng Lượng & Vòng Đời Pin",
        "left_card": {
            "title": "Mô Hình Toán Cân Bằng Năng Lượng",
            "bullets": [
                [("• ", False), ("Công thức tiêu thụ hàng ngày (E_daily): ", True), ("E = I_sleep × t_sleep + I_active × t_active + I_tx × t_tx")],
                [("• ", False), ("Tính toán thực tế: ", True), ("Ngủ sâu (23.95h × 0.185mA) = 4.43 mAh; Chụp ảnh (2 lần × 0.45s × 68mA) = 0.017 mAh; Truyền NB-IoT (2 lần × 6.2s × 120mA) = 0.413 mAh. ", False), ("Tổng tiêu thụ: ~4.86 mAh/ngày", True), (".")],
                [("• ", False), ("Năng lượng thu được từ Tua-bin: ", True), ("Lưu lượng sinh hoạt trung bình 30 Lít/ngày (tốc độ 6 L/min -> chảy 5 phút = 300s). Dòng sạc trung bình 65 mA. ", False), ("Năng lượng sạc: 65mA × (300/3600)h = 5.42 mAh/ngày", True), (".")],
                [("• ", False), ("Kết luận cân bằng: ", True), ("Năng lượng nạp (5.42 mAh) > Năng lượng tiêu thụ (4.86 mAh) -> ", False), ("Thặng dư +0.56 mAh/ngày (Pin tự sạc đầy liên tục)", True), (".")],
            ]
        },
        "right_box": {
            "fig_title": "Đồ Thị Mô Phỏng Dung Lượng Pin Theo Thời Gian",
            "points": [
                "Trường hợp 1 (Có xả nước sinh hoạt bình thường): Dung lượng pin luôn duy trì ở mức 95% - 100%.",
                "Trường hợp 2 (Khách hàng vắng nhà 1 tháng không xả nước): Pin Li-ion 3000mAh suy giảm 4.86 mAh × 30 ngày = 145.8 mAh (chỉ mất ~4.8% dung lượng).",
                "Trường hợp 3 (Hoàn toàn không có nước xả): Pin 3000mAh duy trì hoạt động độc lập hơn 600 ngày!",
                "Kết luận: Hệ thống hoàn toàn miễn nhiễm với rủi ro cạn kiệt năng lượng."
            ],
            "hint": "(Gợi ý: Chèn đồ thị mô phỏng suy giảm dung lượng pin và sạc bù từ tua-bin)"
        }
    },

    {
        "type": "two_column",
        "title": "Phụ Lục 2: Tiêu Chuẩn Vệ Sinh An Toàn Nước Uống",
        "left_card": {
            "title": "Đảm Bảo Chất Lượng Nguồn Nước Sinh Hoạt",
            "bullets": [
                [("• ", False), ("Vật liệu chế tạo Tua-bin: ", True), ("Thân tua-bin và cánh quạt được làm từ ", False), ("nhựa kỹ thuật thực phẩm POM / ABS nguyên sinh", True), (", không chứa chì và kim loại nặng độc hại.")],
                [("• ", False), ("Tiêu chuẩn tương thích quốc tế: ", True), ("Đáp ứng định hướng tiêu chuẩn an toàn vật liệu tiếp xúc nước sinh hoạt ", False), ("NSF/ANSI 61 và WRAS", True), (".")],
                [("• ", False), ("Độ sụt áp suất dòng chảy: ", True), ("Tua-bin mini có đường kính ống tiêu chuẩn Phi 21 (G1/2 inch). Tại lưu lượng tối đa 10 L/phút, độ sụt áp ", False), ("ΔP < 0.05 MPa", True), (", không ảnh hưởng áp lực nước vòi sinh hoạt.")],
                [("• ", False), ("Độ bền cơ học: ", True), ("Chịu được áp suất thủy tĩnh danh định ", False), ("1.2 MPa (12 bar)", True), (", chống rò rỉ tại các đầu ren nối cao su chịu dầu EPDM.")],
            ]
        },
        "right_box": {
            "fig_title": "Cấu Tạo Cơ Học Khép Kín Của Tua-Bin Thủy Lực",
            "points": [
                "Cánh quạt ly tâm (Impeller): Truyền động từ trường cách ly hoàn toàn với cuộn dây stator.",
                "Buồng nước kín (Sealed Chamber): Không có tiếp xúc điện với dòng nước, chống rò rỉ điện tuyệt đối.",
                "Thử nghiệm áp lực: Chịu áp lực nước thử nghiệm 1.75 MPa trong 15 phút không nứt vỡ.",
                "Gioăng làm kín: Sử dụng ron cao su chịu nước EPDM tiêu chuẩn ngành cấp nước."
            ],
            "hint": "(Gợi ý: Chèn bản vẽ mặt cắt cơ khí tua-bin nước F50 hoặc ảnh thử nghiệm áp lực)"
        }
    },

    {
        "type": "two_column",
        "title": "Phụ Lục 3: Cơ Chế Bảo Mật & Toàn Vẹn Dữ Liệu Toàn Trình",
        "left_card": {
            "title": "Bảo Mật Từ Thiết Bị Biên Đến Đám Mây",
            "bullets": [
                [("• ", False), ("Bảo vệ Thiết bị Biên (Hardware Security): ", True), ("Khóa bí mật thiết bị (Device Secret Key) được nạp vào vùng nhớ ", False), ("eFuse chỉ ghi một lần (One-Time Programmable)", True), (" của ESP32-S3, chống trích xuất mã nguồn.")],
                [("• ", False), ("Bảo mật đường truyền (Network Security): ", True), ("Sử dụng giao thức ", False), ("MQTTS qua lớp bảo mật TLS v1.3", True), (" mã hóa toàn bộ dữ liệu telemetry và hình ảnh qua mạng di động.")],
                [("• ", False), ("Xác thực & Chống giả mạo bản tin: ", True), ("Mỗi bản tin gửi lên đều đi kèm chữ ký xác thực ", False), ("HMAC-SHA256", True), (" và Timestamp, chống tấn công phát lại (Replay Attack).")],
                [("• ", False), ("Chống gian lận chỉ số: ", True), ("Lưu vết ảnh gốc vĩnh viễn trên Cloud Storage có mã băm toàn vẹn SHA-256 đối soát khi có tranh chấp pháp lý.")],
            ]
        },
        "right_box": {
            "fig_title": "Mô Hình Bảo Mật 3 Lớp Từ Biên Tới Ứng Dụng",
            "points": [
                "Lớp 1 (Hardware Edge): ESP32-S3 Secure Boot + Flash Encryption + eFuse.",
                "Lớp 2 (Transport Channel): TLS v1.3 / MQTTS mã hóa AES-128 đường truyền.",
                "Lớp 3 (Cloud & Data): Quản lý phiên JWT, phân quyền RBAC và mã băm SHA-256 ảnh gốc.",
                "Đánh giá an ninh: Hệ thống đáp ứng các tiêu chuẩn bảo mật cho hạ tầng đo lường thông minh (AMI)."
            ],
            "hint": "(Gợi ý: Chèn sơ đồ mô hình bảo mật 3 lớp toàn trình End-to-End Security)"
        }
    }
]

print(f"Loaded {len(SLIDES)} slides for Canva-optimized deck successfully")
