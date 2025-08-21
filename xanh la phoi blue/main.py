from nicegui import ui

# ======= CSS =======
ui.add_head_html('''
<style>
    body {
        background-color: #0f172a; /* nền xanh đậm sang trọng */
    }
    .blue-card {
        width: 100%;
        max-width: 900px;
        border-radius: 24px;
        padding: 3rem;
        background: linear-gradient(135deg, #1e3a8a, #0f172a, #1e3a8a);
        box-shadow: 0 0 20px rgba(96,165,250,0.25);
        backdrop-filter: blur(12px);
        transition: all 0.4s ease-in-out;
        margin: 0 auto; /* luôn căn giữa */
    }
    .blue-card:hover {
        box-shadow: 0 0 30px rgba(209,213,219,0.45);
        transform: translateY(-4px);
    }
    .hero-title {
        font-size: 6rem;
        font-weight: 900;
        background: linear-gradient(90deg, #16a34a, #22c55e, #4ade80, #84cc16, #a3e635); /* vẫn giữ xanh lá */
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientFlow 12s linear infinite, shine 8s ease-in-out infinite;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7),
                     0 0 12px rgba(34,197,94,0.4),
                     0 0 20px rgba(132,204,22,0.4);
    }
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes shine {
        0%, 90%, 100% { filter: brightness(1); }
        45% { filter: brightness(1.6); }
    }
</style>
''')

# ======= Hero Section =======
with ui.column().classes('w-full items-center justify-center text-center text-white mt-12'):
    ui.label('SmartMacroAI').classes(
        'hero-title mb-4 text-9xl font-extrabold drop-shadow-lg'
    )
    ui.label('Tự động hoá thông minh với AI').classes(
        'text-2xl italic text-gray-300 mb-10'
    )

# ======= Video Section (Royal Blue Card) =======
with ui.column().classes('w-full items-center mt-10'):
    with ui.card().classes('blue-card'):
        with ui.row().classes("w-full justify-between items-center mb-6"):
            ui.label("🎥 SmartMacroAI – Demo trực tiếp").classes(
                "text-3xl font-bold bg-gradient-to-r from-blue-300 to-gray-200 "
                "bg-clip-text text-transparent drop-shadow-lg"
            )
            ui.link("⬇️ Tải ngay", "https://github.com/smartmacroai/SmartMacroAI") \
                .props('target=_blank') \
                .classes(
                    "px-6 py-2 rounded-lg font-semibold text-lg no-underline "
                    "bg-gradient-to-r from-blue-400 to-sky-600 "
                    "text-white shadow-md hover:scale-110 hover:shadow-[0_0_20px_rgba(96,165,250,0.6)] "
                    "transition-all duration-300"
                )

        ui.element('iframe') \
            .props('src=https://www.youtube.com/embed/IHlVkJaOUCg') \
            .props('width=100% style="aspect-ratio:16/9;" frameborder=0 allow=accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share allowfullscreen') \
            .classes('rounded-2xl shadow-xl')

# ======= Features Section (Royal Blue Card) =======
with ui.column().classes('w-full items-center mt-20'):
    with ui.card().classes('blue-card text-center'):
        ui.label('🚀 SmartMacroAI – Giải pháp tự động hóa thông minh cho Windows 10/11 64-bit') \
            .classes(
                'text-4xl font-extrabold mb-8 '
                'bg-gradient-to-r from-blue-300 to-gray-200 '
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
                    'text-lg text-gray-100 transition duration-300 hover:text-blue-400 hover:translate-x-1'
                )

        ui.separator().classes('my-10 border-gray-700')

        ui.label('📌 Thông tin nhà phát triển:') \
            .classes(
                'text-2xl font-bold mb-6 '
                'bg-gradient-to-r from-blue-300 to-gray-200 '
                'bg-clip-text text-transparent drop-shadow-lg'
            )

        ui.label('👤 Tên: Nguyễn Văn Đức').classes('text-white')
        ui.label('📧 Email: smartmacroai@gmail.com').classes('text-white')
        ui.label('📱 Số điện thoại/Zalo: 0985205375').classes('text-white')

        with ui.row().classes('justify-center mt-6 space-x-8'):
            ui.link('🌐 Fanpage Facebook', 'https://www.facebook.com/smartmacroai') \
                .props('target=_blank') \
                .classes('text-blue-300 hover:text-gray-300 transition duration-300')
            ui.link('👥 Cộng đồng Facebook', 'https://www.facebook.com/groups/smartmacroai') \
                .props('target=_blank') \
                .classes('text-blue-300 hover:text-gray-300 transition duration-300')

ui.run(reload=False)
