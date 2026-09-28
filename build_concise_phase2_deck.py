# -*- coding: utf-8 -*-
"""
Script dựng hoàn chỉnh bộ slide 27 trang chuẩn Rubric Khoa CE (Giai đoạn 2)
Tối ưu hóa 100% cho Canva Import:
- BỎ hoàn toàn số slide (không đánh số)
- BỎ các chữ nhỏ/nhãn Rubric phía trên tiêu đề
- BỎ các bảng XML phức tạp (chuyển sang Card / Cột trực quan tương thích 100% Canva)
- Cỡ chữ to rõ: Tiêu đề 38pt, Thẻ 26-28pt, Nội dung thường 25pt
- Slide mở màn chuẩn ảnh nền gốc image1.png từ GĐ1
"""

import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from concise_slides_data import SLIDES

# BẢNG MÀU CHUẨN DESIGN SYSTEM
COLOR_NAVY       = RGBColor(0, 59, 115)     # #003B73 - Xanh Bách Khoa
COLOR_PRIMARY    = RGBColor(2, 132, 199)    # #0284C7 - Sky Blue hiện đại
COLOR_DARK       = RGBColor(30, 41, 59)     # #1E293B - Slate đậm cho text chính
COLOR_MUTED      = RGBColor(100, 116, 139)  # #64748B - Slate xám nhạt
COLOR_BG_CARD    = RGBColor(255, 255, 255)  # Trắng tinh khiết
COLOR_BORDER     = RGBColor(203, 213, 225)  # #CBD5E1 - Viền card xám xanh
COLOR_PLACEHOLDER= RGBColor(248, 250, 252)  # #F8FAFC - Nền khung chèn ảnh
COLOR_ACCENT_GREEN = RGBColor(16, 185, 129) # #10B981 - Xanh lá điểm nhấn
COLOR_HIGHLIGHT_BG = RGBColor(240, 249, 255)# #F0F9FF - Nền highlight nhẹ
COLOR_SUCCESS_BG   = RGBColor(236, 253, 245)# #ECFDF5 - Nền xanh lá nhạt

SLIDE_WIDTH  = Inches(20.0)
SLIDE_HEIGHT = Inches(11.25)

def apply_text_runs(paragraph, text_runs, default_size=25, default_color=COLOR_DARK):
    paragraph.font.size = Pt(default_size)
    paragraph.font.name = "Roboto"
    for r_item in text_runs:
        if isinstance(r_item, str):
            run = paragraph.add_run()
            run.text = r_item
            run.font.bold = False
            run.font.size = Pt(default_size)
            run.font.color.rgb = default_color
            run.font.name = "Roboto"
        elif isinstance(r_item, tuple):
            text = r_item[0]
            bold = r_item[1] if len(r_item) > 1 else False
            color = r_item[2] if len(r_item) > 2 and r_item[2] else default_color
            size = r_item[3] if len(r_item) > 3 and r_item[3] else default_size
            run = paragraph.add_run()
            run.text = text
            run.font.bold = bold
            run.font.size = Pt(size)
            run.font.color.rgb = color
            run.font.name = "Roboto"

def add_clean_header(slide, title_text):
    """Header tối giản, sang trọng, không nhãn nhỏ, không số slide"""
    # 1. Tiêu đề slide lớn, rõ ràng (38pt Bold)
    title_box = slide.shapes.add_textbox(Inches(1.0), Inches(0.65), Inches(18.0), Inches(0.85))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(38)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_NAVY
    p_title.font.name = "Roboto"

    # 2. Thanh kẻ phân cách hiện đại
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.55), Inches(18.0), Inches(0.06))
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_PRIMARY
    line.line.color.rgb = COLOR_PRIMARY

def build_presentation(output_path):
    prs = pptx.Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    blank_layout = prs.slide_layouts[6]
    total_slides = len(SLIDES)

    print(f"Bắt đầu dựng {total_slides} slides chuẩn Canva...")

    for idx, s_data in enumerate(SLIDES):
        s_type = s_data["type"]
        slide = prs.slides.add_slide(blank_layout)

        # ---------------------------------------------------------
        # 1. SLIDE BÌA (FORMAT NGUYÊN BẢN GĐ1 - KHÔNG SỐ SLIDE)
        # ---------------------------------------------------------
        if s_type == "title":
            bg_path = os.path.join("extracted_figures", "image1.png")
            if os.path.exists(bg_path):
                slide.shapes.add_picture(bg_path, 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT)

            # Trường ĐH
            b_head = slide.shapes.add_textbox(Inches(3.0), Inches(1.8), Inches(14.0), Inches(0.6))
            p = b_head.text_frame.paragraphs[0]
            p.text = "ĐẠI HỌC QUỐC GIA TP.HCM - TRƯỜNG ĐẠI HỌC BÁCH KHOA"
            p.font.size = Pt(28)
            p.font.bold = True
            p.font.color.rgb = COLOR_NAVY
            p.alignment = PP_ALIGN.CENTER
            p.font.name = "Roboto"

            # Tên đề tài
            b_topic = slide.shapes.add_textbox(Inches(1.5), Inches(2.4), Inches(17.0), Inches(2.3))
            b_topic.text_frame.word_wrap = True
            p_top = b_topic.text_frame.paragraphs[0]
            p_top.text = s_data["topic"]
            p_top.font.size = Pt(44)
            p_top.font.bold = True
            p_top.font.color.rgb = COLOR_NAVY
            p_top.alignment = PP_ALIGN.CENTER
            p_top.font.name = "Roboto"

            # Subtitle
            b_sub = slide.shapes.add_textbox(Inches(2.0), Inches(5.1), Inches(16.0), Inches(0.8))
            p_sub = b_sub.text_frame.paragraphs[0]
            p_sub.text = s_data["sub_topic"]
            p_sub.font.size = Pt(32)
            p_sub.font.bold = True
            p_sub.font.color.rgb = COLOR_PRIMARY
            p_sub.alignment = PP_ALIGN.CENTER
            p_sub.font.name = "Roboto"

            # Box GVHD & Hội đồng
            b_adv = slide.shapes.add_textbox(Inches(2.8), Inches(6.8), Inches(7.5), Inches(1.8))
            tf_adv = b_adv.text_frame
            tf_adv.word_wrap = True
            p1 = tf_adv.paragraphs[0]
            p1.text = s_data["advisor"]
            p1.font.size = Pt(26)
            p1.font.bold = True
            p1.font.color.rgb = COLOR_DARK
            p1.font.name = "Roboto"
            p1.space_after = Pt(12)

            p2 = tf_adv.add_paragraph()
            p2.text = s_data["council"]
            p2.font.size = Pt(26)
            p2.font.bold = True
            p2.font.color.rgb = COLOR_DARK
            p2.font.name = "Roboto"

            # Box Sinh viên thực hiện
            b_stu = slide.shapes.add_textbox(Inches(11.0), Inches(6.8), Inches(6.5), Inches(2.2))
            tf_stu = b_stu.text_frame
            tf_stu.word_wrap = True
            for s_i, stu_name in enumerate(s_data["students"]):
                p_s = tf_stu.paragraphs[0] if s_i == 0 else tf_stu.add_paragraph()
                prefix = "SVTH:  " if s_i == 0 else "          "
                p_s.text = f"{prefix}{stu_name}"
                p_s.font.size = Pt(26)
                p_s.font.bold = True
                p_s.font.color.rgb = COLOR_DARK
                p_s.font.name = "Roboto"
                p_s.space_after = Pt(8)

        # ---------------------------------------------------------
        # 2. SLIDE 2 CỘT (CARD TRÁI + KHUNG PLACEHOLDER PHẢI)
        # ---------------------------------------------------------
        elif s_type == "two_column":
            add_clean_header(slide, s_data["title"])

            # --- CARD TRÁI ---
            card_left = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.8), Inches(9.2), Inches(8.8))
            card_left.fill.solid()
            card_left.fill.fore_color.rgb = COLOR_BG_CARD
            card_left.line.color.rgb = COLOR_BORDER
            card_left.line.width = Pt(1.5)

            tb_left = slide.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(8.8), Inches(8.4))
            tf_l = tb_left.text_frame
            tf_l.word_wrap = True

            p_lt = tf_l.paragraphs[0]
            p_lt.text = s_data["left_card"]["title"]
            p_lt.font.size = Pt(28)
            p_lt.font.bold = True
            p_lt.font.color.rgb = COLOR_NAVY
            p_lt.font.name = "Roboto"
            p_lt.space_after = Pt(20)

            for b_runs in s_data["left_card"]["bullets"]:
                p_b = tf_l.add_paragraph()
                apply_text_runs(p_b, b_runs, default_size=25, default_color=COLOR_DARK)
                p_b.space_after = Pt(18)

            # --- CARD PHẢI (KHUNG PLACEHOLDER) ---
            r_box = s_data["right_box"]
            card_right = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.6), Inches(1.8), Inches(8.4), Inches(8.8))
            card_right.fill.solid()
            card_right.fill.fore_color.rgb = COLOR_PLACEHOLDER
            card_right.line.color.rgb = COLOR_PRIMARY
            card_right.line.width = Pt(2.5)

            tb_right = slide.shapes.add_textbox(Inches(10.8), Inches(2.0), Inches(8.0), Inches(8.4))
            tf_r = tb_right.text_frame
            tf_r.word_wrap = True

            p_rb0 = tf_r.paragraphs[0]
            p_rb0.text = "[ 📷 KHUNG CHÈN HÌNH ẢNH SƠ ĐỒ ]"
            p_rb0.font.size = Pt(24)
            p_rb0.font.bold = True
            p_rb0.font.color.rgb = COLOR_PRIMARY
            p_rb0.alignment = PP_ALIGN.CENTER
            p_rb0.font.name = "Roboto"
            p_rb0.space_after = Pt(14)

            p_rb1 = tf_r.add_paragraph()
            p_rb1.text = r_box["fig_title"]
            p_rb1.font.size = Pt(26)
            p_rb1.font.bold = True
            p_rb1.font.color.rgb = COLOR_NAVY
            p_rb1.alignment = PP_ALIGN.CENTER
            p_rb1.font.name = "Roboto"
            p_rb1.space_after = Pt(20)

            for pt in r_box["points"]:
                p_pt = tf_r.add_paragraph()
                p_pt.text = f"•  {pt}"
                p_pt.font.size = Pt(23)
                p_pt.font.color.rgb = COLOR_DARK
                p_pt.font.name = "Roboto"
                p_pt.space_after = Pt(14)

            p_hint = tf_r.add_paragraph()
            p_hint.text = r_box["hint"]
            p_hint.font.size = Pt(20)
            p_hint.font.italic = True
            p_hint.font.color.rgb = COLOR_MUTED
            p_hint.alignment = PP_ALIGN.CENTER
            p_hint.font.name = "Roboto"
            p_hint.space_before = Pt(18)

        # ---------------------------------------------------------
        # 3. SLIDE 3 CỘT SO SÁNH (THAY THẾ BẢNG ĐỂ CANVA KHÔNG LỖI)
        # ---------------------------------------------------------
        elif s_type == "three_column_compare":
            add_clean_header(slide, s_data["title"])

            col_widths = Inches(5.7)
            col_gap = Inches(0.45)
            left_base = Inches(1.0)

            for c_i, col_data in enumerate(s_data["columns"]):
                pos_x = left_base + c_i * (col_widths + col_gap)
                is_hi = col_data.get("is_highlight", False)

                card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_x, Inches(1.8), col_widths, Inches(8.8))
                card.fill.solid()
                card.fill.fore_color.rgb = COLOR_HIGHLIGHT_BG if is_hi else COLOR_BG_CARD
                card.line.color.rgb = COLOR_PRIMARY if is_hi else COLOR_BORDER
                card.line.width = Pt(3.0 if is_hi else 1.5)

                tb = slide.shapes.add_textbox(pos_x + Inches(0.2), Inches(2.0), col_widths - Inches(0.4), Inches(8.4))
                tf = tb.text_frame
                tf.word_wrap = True

                # Badge
                p_b = tf.paragraphs[0]
                p_b.text = col_data["badge"]
                p_b.font.size = Pt(20)
                p_b.font.bold = True
                p_b.font.color.rgb = COLOR_ACCENT_GREEN if is_hi else COLOR_MUTED
                p_b.alignment = PP_ALIGN.CENTER
                p_b.font.name = "Roboto"
                p_b.space_after = Pt(10)

                # Title
                p_t = tf.add_paragraph()
                p_t.text = col_data["title"]
                p_t.font.size = Pt(26)
                p_t.font.bold = True
                p_t.font.color.rgb = COLOR_NAVY
                p_t.alignment = PP_ALIGN.CENTER
                p_t.font.name = "Roboto"
                p_t.space_after = Pt(20)

                # Items
                for label, val in col_data["items"]:
                    p_lbl = tf.add_paragraph()
                    p_lbl.text = f"▪ {label}"
                    p_lbl.font.size = Pt(22)
                    p_lbl.font.bold = True
                    p_lbl.font.color.rgb = COLOR_PRIMARY if is_hi else COLOR_DARK
                    p_lbl.font.name = "Roboto"

                    p_val = tf.add_paragraph()
                    p_val.text = f"   {val}"
                    p_val.font.size = Pt(22)
                    p_val.font.color.rgb = COLOR_DARK
                    p_val.font.name = "Roboto"
                    p_val.space_after = Pt(12)

        # ---------------------------------------------------------
        # 4. SLIDE 4-GRID (2x2 CARDS CHO ĐÁNH GIÁ 4 TRỤ CỘT / ĐO KIỂM)
        # ---------------------------------------------------------
        elif s_type == "four_grid":
            add_clean_header(slide, s_data["title"])

            grid_positions = [
                (Inches(1.0), Inches(1.85)),   # Top Left
                (Inches(10.2), Inches(1.85)),  # Top Right
                (Inches(1.0), Inches(6.25)),   # Bottom Left
                (Inches(10.2), Inches(6.25))   # Bottom Right
            ]

            card_w = Inches(8.8)
            card_h = Inches(4.2)

            for g_i, c_info in enumerate(s_data["cards"]):
                pos_x, pos_y = grid_positions[g_i]
                c_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_x, pos_y, card_w, card_h)
                c_shape.fill.solid()
                c_shape.fill.fore_color.rgb = COLOR_BG_CARD
                c_shape.line.color.rgb = COLOR_PRIMARY
                c_shape.line.width = Pt(2.0)

                tb = slide.shapes.add_textbox(pos_x + Inches(0.25), pos_y + Inches(0.18), card_w - Inches(0.5), card_h - Inches(0.36))
                tf = tb.text_frame
                tf.word_wrap = True

                p_t = tf.paragraphs[0]
                p_t.text = c_info["title"]
                p_t.font.size = Pt(26)
                p_t.font.bold = True
                p_t.font.color.rgb = COLOR_NAVY
                p_t.font.name = "Roboto"
                p_t.space_after = Pt(12)

                for b in c_info["bullets"]:
                    p_b = tf.add_paragraph()
                    p_b.text = f"•  {b}"
                    p_b.font.size = Pt(22)
                    p_b.font.color.rgb = COLOR_DARK
                    p_b.font.name = "Roboto"
                    p_b.space_after = Pt(8)

        # ---------------------------------------------------------
        # 5. SLIDE 2 CỘT ĐỐI SOÁT NHIỆM VỤ (THAY THẾ BẢNG 8 DÒNG)
        # ---------------------------------------------------------
        elif s_type == "two_column_tasks":
            add_clean_header(slide, s_data["title"])

            col_w = Inches(8.8)
            card_h = Inches(7.5)

            # Cột 1
            c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.8), col_w, card_h)
            c1.fill.solid()
            c1.fill.fore_color.rgb = COLOR_BG_CARD
            c1.line.color.rgb = COLOR_BORDER
            c1.line.width = Pt(1.5)

            tb1 = slide.shapes.add_textbox(Inches(1.2), Inches(1.95), col_w - Inches(0.4), card_h - Inches(0.3))
            tf1 = tb1.text_frame
            tf1.word_wrap = True

            pt1 = tf1.paragraphs[0]
            pt1.text = s_data["col1_title"]
            pt1.font.size = Pt(26)
            pt1.font.bold = True
            pt1.font.color.rgb = COLOR_NAVY
            pt1.font.name = "Roboto"
            pt1.space_after = Pt(16)

            for t_title, t_desc, t_st in s_data["col1_tasks"]:
                p_task = tf1.add_paragraph()
                p_task.text = f"✔ {t_title}"
                p_task.font.size = Pt(22)
                p_task.font.bold = True
                p_task.font.color.rgb = COLOR_PRIMARY
                p_task.font.name = "Roboto"

                p_desc = tf1.add_paragraph()
                p_desc.text = f"   {t_desc}  →  [{t_st}]"
                p_desc.font.size = Pt(21)
                p_desc.font.color.rgb = COLOR_DARK
                p_desc.font.name = "Roboto"
                p_desc.space_after = Pt(12)

            # Cột 2
            c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.2), Inches(1.8), col_w, card_h)
            c2.fill.solid()
            c2.fill.fore_color.rgb = COLOR_BG_CARD
            c2.line.color.rgb = COLOR_BORDER
            c2.line.width = Pt(1.5)

            tb2 = slide.shapes.add_textbox(Inches(10.4), Inches(1.95), col_w - Inches(0.4), card_h - Inches(0.3))
            tf2 = tb2.text_frame
            tf2.word_wrap = True

            pt2 = tf2.paragraphs[0]
            pt2.text = s_data["col2_title"]
            pt2.font.size = Pt(26)
            pt2.font.bold = True
            pt2.font.color.rgb = COLOR_NAVY
            pt2.font.name = "Roboto"
            pt2.space_after = Pt(16)

            for t_title, t_desc, t_st in s_data["col2_tasks"]:
                p_task = tf2.add_paragraph()
                p_task.text = f"✔ {t_title}"
                p_task.font.size = Pt(22)
                p_task.font.bold = True
                p_task.font.color.rgb = COLOR_PRIMARY
                p_task.font.name = "Roboto"

                p_desc = tf2.add_paragraph()
                p_desc.text = f"   {t_desc}  →  [{t_st}]"
                p_desc.font.size = Pt(21)
                p_desc.font.color.rgb = COLOR_DARK
                p_desc.font.name = "Roboto"
                p_desc.space_after = Pt(12)

            # Khung tổng kết hoàn thành ở dưới
            sum_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(9.55), Inches(18.0), Inches(1.05))
            sum_card.fill.solid()
            sum_card.fill.fore_color.rgb = COLOR_SUCCESS_BG
            sum_card.line.color.rgb = COLOR_ACCENT_GREEN
            sum_card.line.width = Pt(2.0)

            tb_s = slide.shapes.add_textbox(Inches(1.2), Inches(9.65), Inches(17.6), Inches(0.85))
            p_s = tb_s.text_frame.paragraphs[0]
            p_s.text = s_data["summary"]
            p_s.font.size = Pt(24)
            p_s.font.bold = True
            p_s.font.color.rgb = RGBColor(6, 95, 70)
            p_s.alignment = PP_ALIGN.CENTER
            p_s.font.name = "Roboto"

        # ---------------------------------------------------------
        # 6. SLIDE Q&A / KẾT THÚC
        # ---------------------------------------------------------
        elif s_type == "qa":
            add_clean_header(slide, s_data["title"])

            box_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.5), Inches(2.2), Inches(15.0), Inches(7.8))
            box_shape.fill.solid()
            box_shape.fill.fore_color.rgb = COLOR_BG_CARD
            box_shape.line.color.rgb = COLOR_PRIMARY
            box_shape.line.width = Pt(3.0)

            tb = slide.shapes.add_textbox(Inches(3.0), Inches(2.8), Inches(14.0), Inches(6.5))
            tf = tb.text_frame
            tf.word_wrap = True

            p1 = tf.paragraphs[0]
            p1.text = "CHÂN THÀNH CẢM ƠN QUÝ THẦY CÔ"
            p1.font.size = Pt(40)
            p1.font.bold = True
            p1.font.color.rgb = COLOR_NAVY
            p1.alignment = PP_ALIGN.CENTER
            p1.font.name = "Roboto"
            p1.space_after = Pt(20)

            p2 = tf.add_paragraph()
            p2.text = "VÀ CÁC THÀNH VIÊN HỘI ĐỒNG ĐÃ LẮNG NGHE BÁO CÁO"
            p2.font.size = Pt(28)
            p2.font.bold = True
            p2.font.color.rgb = COLOR_PRIMARY
            p2.alignment = PP_ALIGN.CENTER
            p2.font.name = "Roboto"
            p2.space_after = Pt(40)

            p3 = tf.add_paragraph()
            p3.text = "KÍNH MỜI QUÝ THẦY CÔ ĐẶT CÂU HỎI PHẢN BIỆN"
            p3.font.size = Pt(34)
            p3.font.bold = True
            p3.font.color.rgb = COLOR_ACCENT_GREEN
            p3.alignment = PP_ALIGN.CENTER
            p3.font.name = "Roboto"
            p3.space_after = Pt(40)

            p4 = tf.add_paragraph()
            p4.text = "HỘI ĐỒNG 4L KỸ THUẬT MÁY TÍNH - KHOA KHOA HỌC & KỸ THUẬT MÁY TÍNH\nTRƯỜNG ĐẠI HỌC BÁCH KHOA - ĐHQG TP.HCM"
            p4.font.size = Pt(24)
            p4.font.color.rgb = COLOR_MUTED
            p4.alignment = PP_ALIGN.CENTER
            p4.font.name = "Roboto"

    prs.save(output_path)
    file_size = os.path.getsize(output_path)
    print(f"Đã lưu thành công file '{output_path}' ({file_size:,} bytes, {total_slides} slides - Canva Ready!)")

if __name__ == "__main__":
    out_file = "Bao_Cao_LVTN_Giai_Doan_2_Chuan_Format_Giai_Doan_1.pptx"
    build_presentation(out_file)
