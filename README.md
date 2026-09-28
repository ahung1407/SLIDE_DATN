# HỆ THỐNG ĐỒNG HỒ NƯỚC THÔNG MINH IOT THU THẬP NĂNG LƯỢNG KẾT HỢP TRÍ TUỆ NHÂN TẠO
## BÁO CÁO LUẬN VĂN TỐT NGHIỆP NGÀNH KỸ THUẬT MÁY TÍNH (GIAI ĐOẠN 2 - BẢO VỆ CUỐI)
**Trường Đại học Bách Khoa – ĐHQG TP.HCM**  
**Khoa Khoa học và Kỹ thuật Máy tính (CE)**  
- **GVHD**: TS. Lê Trọng Nhân  
- **Hội đồng**: 4L Kỹ thuật Máy tính  
- **SVTH**:
  - Nguyễn Minh Hưng (2211367)
  - Lê Quang Trưng (2213730)
  - Nguyễn Văn Huynh (2211315)

---

## 📌 Cấu Trúc Dự Án & File Báo Cáo

| Tên File / Thư Mục | Mô Tả |
| :--- | :--- |
| **`Bao_Cao_LVTN_Giai_Doan_2_Chuan_Format_Giai_Doan_1.pptx`** | File Slide chính thức 27 trang (Tối ưu hóa Canva, không lỗi import, không số trang, cỡ chữ to >= 25pt, thẻ trực quan). |
| **`GHI_CHU_THUYET_TRINH_LVTN_GIAI_DOAN_2.md`** | Kịch bản thuyết trình & ghi chú chi tiết cho 3 sinh viên tương ứng 27 slide. |
| **`build_concise_phase2_deck.py`** | Script Python tự động sinh file slide PowerPoint từ dữ liệu. |
| **`concise_slides_data.py`** | Dữ liệu cấu trúc 27 slide (nội dung, thông số đo kiểm, phân chia 3 phần). |
| **`extracted_figures/`** | Thư mục chứa hình nền gốc Slide 1 (`image1.png`) và các ảnh sơ đồ kỹ thuật. |
| **`HK253_DATN_006_2211367_2213730_2211315.pdf`** | Toàn văn Báo cáo Luận văn Tốt nghiệp Giai đoạn 2. |
| **`Báo cáo đồ án chuyên ngành giai đoạn 1.*`** | Báo cáo & Slide mẫu Giai đoạn 1. |
| **`Form_*` / `Phieu Danh Gia*`** | Các file Rubric chấm điểm ABET của Khoa CE (GVHD, GVPB, Hội đồng). |

---

## 🎯 Phân Chia 3 Phần Thuyết Trình
- **Mở đầu (Chung cả nhóm)**: Đặt vấn đề, mục tiêu, so sánh giải pháp (Trade-off), kiến trúc 4 phân tầng (Slide 1 - 4).
- **Phần 1 (Sinh viên 1)**: Thiết bị Biên ESP32-S3 & Quản lý Năng lượng Harvester (Slide 5 - 9).
- **Phần 2 (Sinh viên 2)**: Hệ thống IoT Truyền thông NB-IoT & Cloud Backend Spring Boot (Slide 10 - 14).
- **Phần 3 (Sinh viên 3)**: Trí tuệ Nhân tạo AI OCR & Phân tích Rò rỉ Nước (Slide 15 - 19).
- **Tổng hợp & Đánh giá Rubric (Chung cả nhóm)**: Đo kiểm chuyên môn, 4 trụ cột lợi ích MT/KT/XH, đối soát 100% nhiệm vụ đề tài, kết luận & Q&A (Slide 20 - 24).
- **Phụ lục Q&A (Backup phản biện)**: Cân bằng năng lượng pin, an toàn nước NSF/ANSI 61, bảo mật toàn trình (Slide 25 - 27).

---

## 🛠 Hướng Dẫn Tái Tạo Slide (Nếu Cần Chỉnh Sửa)
Cài đặt thư viện yêu cầu:
```bash
pip install python-pptx
```
Chạy lệnh tạo slide:
```bash
python build_concise_phase2_deck.py
```
File PowerPoint mới sẽ được sinh ra ngay tại thư mục gốc và có thể kéo thả trực tiếp vào Canva để thuyết trình!
