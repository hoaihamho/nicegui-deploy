from nicegui import ui

# ======= CSS =======
ui.add_head_html('''
<style>
    body {
        background-color: #1a1a1a; /* nền tối sang trọng */
    }
    .green-card {
        width: 100%;
        max-width: 1100px;
        border-radius: 24px;
        padding: 3rem;
        background: linear-gradient(135deg, #14532d, #0f172a, #14532d);
        box-shadow: 0 0 20px rgba(34,197,94,0.25);
        backdrop-filter: blur(12px);
        transition: all 0.4s ease-in-out;
    }
    .green-card:hover {
        box-shadow: 0 0 30px rgba(34,197,94,0.45);
        transform: translateY(-4px);
    }
    .hero-title {
        font-size: 6rem;
        font-weight: 900;
        background: linear-gradient(90deg, #16a34a, #22c55e, #4ade80, #08c97f, #04d499);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientFlow 12s linear infinite, shine 8s ease-in-out infinite;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7),
                     0 0 12px rgba(34,197,94,0.4),
                     0 0 20px rgba(132,204,22,0.4);
    }
    /* Màn hình 2K (≥ 2560px) */
    @media (min-width: 2560px) {
        .hero-title {
            font-size: 8rem;
        }
    }

    /* Màn hình 4K (≥ 3840px) */
    @media (min-width: 3840px) {
        .hero-title {
            font-size: 10rem;
        }
    }
    /* Laptop */
    @media (max-width: 1440px) {
        .hero-title {
            font-size: 5rem;
        }
    }

    /* Tablet */
    @media (max-width: 1024px) {
        .hero-title {
            font-size: 4rem;
        }
    }

    /* Điện thoại */
    @media (max-width: 640px) {
        .hero-title {
            font-size: 2.5rem;
        }
    }
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes shine {
        0%, 90%, 100% { filter: brightness(1); }
        45% { filter: brightness(1.8); }
    }
</style>
''')

# ======= Hero Section =======
with ui.column().classes('w-full items-center justify-center text-center text-white mt-2'):
    ui.label('SmartMacroAI').classes(
        'hero-title mb-4 text-9xl font-extrabold drop-shadow-lg'
    )

# ======= Video Section (dùng chung style Features) =======
with ui.column().classes('w-full items-center mt-2'):
    with ui.card().classes('green-card'):
        # Hàng ngang: Tiêu đề bên trái, nút bên phải
        with ui.row().classes("w-full justify-between items-center mb-6"):
            ui.label("🎥 SmartMacroAI – Tự động hoá thông minh với AI").classes(
                "text-3xl font-bold bg-gradient-to-r from-green-300 to-lime-400 "
                "bg-clip-text text-transparent drop-shadow-lg"
            )
            ui.link("⬇️ Tải ngay", "https://github.com/smartmacroai/SmartMacroAI") \
                .props('target=_blank') \
                .classes(
                    "px-6 py-2 rounded-lg font-semibold text-lg no-underline "
                    "bg-gradient-to-r from-green-400 to-emerald-600 "
                    "text-white shadow-md hover:scale-110 hover:shadow-[0_0_20px_rgba(34,197,94,0.6)] "
                    "transition-all duration-300"
                )

        # Video YouTube bên dưới
        ui.element('iframe') \
            .props('src=https://www.youtube.com/embed/IHlVkJaOUCg') \
            .props('width=100% style="aspect-ratio:16/9;" frameborder=0 allow=accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share allowfullscreen') \
            .classes('rounded-2xl shadow-xl')

# ======= Features Section =======
with ui.column().classes('w-full items-center mt-20'):
    with ui.card().classes('green-card text-center'):
        ui.label('🚀 SmartMacroAI – Giải pháp tự động hóa thông minh cho Windows 10/11 64-bit') \
            .classes(
                'text-4xl font-extrabold mb-8 '
                'bg-gradient-to-r from-green-300 to-lime-400 '
                'bg-clip-text text-transparent drop-shadow-lg'
            )

        ui.label(
            'Trải nghiệm tương lai của sự tiện lợi: kéo & thả để hoàn thành mọi tác vụ nhanh chóng, '
            'ngay cả với người không rành công nghệ cũng chỉ cần vài phút để làm quen.'
        ).classes('text-lg mb-10 text-gray-200 leading-relaxed')

        features = [
            ("⚡", "Dễ sử dụng, bỏ qua bước viết script phức tạp thường thấy ở phần mềm khác"),
            ("🎯", "Nhận diện hình ảnh mạnh mẽ, chính xác cao"),
            ("🔥", "Hiệu suất tối ưu: đa luồng, chạy nền không chiếm chuột"),
            ("⏰", "Lên lịch macro tự động với độ chính xác theo thời gian tuỳ chỉnh"),
            ("🖥️", "Tương thích Windows: Web, giả lập Android, client PC..."),
            ("🧩", "Tạo Macro có điều kiện và không điều kiện linh hoạt..."),
        ]

        with ui.column().classes('items-start space-y-4 text-left mx-auto max-w-2xl'):
            for icon, text in features:
                ui.label(f'{icon} {text}').classes(
                    'text-lg text-gray-100 transition duration-300 hover:text-green-400 hover:translate-x-1'
                )

        ui.separator().classes('my-10 border-gray-700')

        ui.label('📌 Thông tin nhà phát triển:') \
            .classes(
                'text-2xl font-bold mb-6 '
                'bg-gradient-to-r from-green-300 to-lime-400 '
                'bg-clip-text text-transparent drop-shadow-lg'
            )

        ui.label('👤 Tên: Nguyễn Văn Đức').classes('text-white')
        ui.label('📧 Email: smartmacroai@gmail.com').classes('text-white')
        ui.label('📱 Số điện thoại/Zalo: 0985205375').classes('text-white')

        with ui.row().classes('justify-center mt-6 space-x-8'):
            ui.link('🌐 Fanpage Facebook', 'https://www.facebook.com/smartmacroai') \
                .props('target=_blank') \
                .classes('text-green-300 hover:text-green-500 transition duration-300')
            ui.link('👥 Cộng đồng Facebook', 'https://www.facebook.com/groups/smartmacroai') \
                .props('target=_blank') \
                .classes('text-green-300 hover:text-green-500 transition duration-300')

ui.run(reload=False)
