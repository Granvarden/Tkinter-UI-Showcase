import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog, colorchooser
import ctypes 

# 1. ฟังก์ชันแก้ภาพแตก (High DPI)
def enable_high_dpi_awareness():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

def create_showcase():
    enable_high_dpi_awareness()

    root = tk.Tk()
    root.title("Tkinter UI Showcas")
    
    # เปลี่ยนการแสดงผลเป็นแบบ ขยายเต็มหน้าต่าง (Maximized Window)
    root.state('zoomed')
    
    # กำหนดสีหลักของโปรแกรม
    BG_COLOR = "#F0F0F0" # สีเทาอ่อน (พื้นหลังแอป)
    WHITE = "#FFFFFF"    # สีขาว (พื้นหลังของการ์ดและเนื้อหา)
    BORDER = "#CCCCCC"   # สีเทาเข้ม (สีขอบ)
    TEXT_COLOR = "#333333"

    root.configure(bg=BG_COLOR)
    
    # 2. ตั้งค่าฟอนต์ Tahoma
    windows_font = ("Tahoma", 11)
    windows_font_bold = ("Tahoma", 11, "bold")
    header_font = ("Tahoma", 16, "bold")
    
    root.option_add("*Font", windows_font)
    
    # ==========================================
    # ปรับแต่ง Theme และกำหนดโทนสี ขาว-เทา
    # ==========================================
    style = ttk.Style()
    style.theme_use('clam') 
    
    # ตั้งค่าสไตล์พื้นฐาน
    style.configure('.', font=windows_font, background=BG_COLOR, foreground=TEXT_COLOR)
    style.configure('Header.TLabel', font=header_font, background=BG_COLOR)
    
    # สไตล์สำหรับเนื้อหาในกล่องสีขาว
    style.configure('White.TLabel', background=WHITE, foreground=TEXT_COLOR)
    style.configure('White.TCheckbutton', background=WHITE, foreground=TEXT_COLOR)
    style.configure('White.TRadiobutton', background=WHITE, foreground=TEXT_COLOR)
    
    style.configure('TNotebook', background=BG_COLOR, borderwidth=0)
    
    # ตั้งค่าตัวแท็บ (เพิ่ม focuscolor เพื่อซ่อนเส้นประตอนคลิก)
    style.configure('TNotebook.Tab', 
                    background="#DCDCDC", 
                    foreground=TEXT_COLOR, 
                    padding=[15, 8], 
                    borderwidth=1, 
                    relief="solid", 
                    bordercolor=BORDER,
                    focuscolor="#DCDCDC") # สีเส้นประให้กลืนกับพื้นหลังตอนยังไม่เลือก
    
    # แก้ไขตำแหน่งและซ่อนเส้นประเมื่อแท็บถูกเลือก
    style.map('TNotebook.Tab', 
              background=[('selected', WHITE)],
              font=[('selected', windows_font_bold)],
              bordercolor=[('selected', BORDER)],
              focuscolor=[('selected', WHITE)], # สีเส้นประให้กลืนกับสีขาวตอนเลือกแล้ว (ซ่อนเส้นประ)
              expand=[('selected', [0, 10, 0, 0])]) # ขยาย ซ้าย 2, บน 5, ขวา 2 พิกเซล เพื่อให้แท็บยกตัวเหนือแท็บอื่น

    # ตั้งค่าสีของ Progressbar ให้เป็นสีเขียวและดูเป็น Flat Design
    style.configure('Horizontal.TProgressbar', 
                    background="#4CAF50",    
                    troughcolor="#E0E0E0",   
                    bordercolor=BORDER,      
                    lightcolor="#4CAF50",    
                    darkcolor="#4CAF50")     

    style.configure('TLabelframe', background=WHITE, bordercolor=BORDER, borderwidth=1)
    style.configure('TLabelframe.Label', background=WHITE, font=windows_font_bold)
    style.configure('White.TFrame', background=WHITE)
    # ==========================================

    def quit_app():
        root.destroy()

    # แถบเมนูด้านบน
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="เปิดไฟล์ใหม่ (New)")
    file_menu.add_command(label="บันทึก (Save)")
    file_menu.add_separator()
    file_menu.add_command(label="ออกจากโปรแกรม", command=quit_app)
    menubar.add_cascade(label="ไฟล์ (File)", menu=file_menu)

    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="เกี่ยวกับโปรแกรม", command=lambda: messagebox.showinfo("About", "Tkinter White-Gray Theme (Full Version)"))
    menubar.add_cascade(label="ช่วยเหลือ (Help)", menu=help_menu)
    root.config(menu=menubar)

    # ส่วนหัวและ Notebook
    header_label = ttk.Label(root, text="รวม UI Widgets แบบจัดเต็ม (โทน ขาว-เทา)", style='Header.TLabel')
    header_label.pack(pady=15)

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True, padx=20, pady=10)

    tab1 = ttk.Frame(notebook, style='White.TFrame')
    tab2 = ttk.Frame(notebook, style='White.TFrame')
    tab3 = ttk.Frame(notebook, style='White.TFrame')
    tab4 = ttk.Frame(notebook, style='White.TFrame')
    tab5 = ttk.Frame(notebook, style='White.TFrame')
    tab6 = ttk.Frame(notebook, style='White.TFrame')
    tab7 = ttk.Frame(notebook, style='White.TFrame') # แท็บใหม่สำหรับ Drag & Drop

    notebook.add(tab1, text="1. Basic & Inputs")
    notebook.add(tab2, text="2. Selections")
    notebook.add(tab3, text="3. Data & Layouts")
    notebook.add(tab4, text="4. Advanced & Dialogs")
    notebook.add(tab5, text="5. Extras & Scroll")
    notebook.add(tab6, text="6. Dashboard (การจัดหน้า)")
    notebook.add(tab7, text="7. Drag & Drop")

    # ==========================================
    # Tab 1: Basic & Inputs
    # ==========================================
    basic_frame = ttk.LabelFrame(tab1, text=" พื้นฐาน (Basic Widgets) ", padding=10)
    basic_frame.pack(fill='x', padx=20, pady=20)
    
    ttk.Label(basic_frame, text="Label: ใช้สำหรับแสดงข้อความ", style='White.TLabel').grid(row=0, column=0, sticky='w', pady=5)
    ttk.Label(basic_frame, text="Entry:", style='White.TLabel').grid(row=1, column=0, sticky='w', pady=5)
    
    entry = ttk.Entry(basic_frame, width=40)
    entry.insert(0, "ช่องกรอกข้อความ 1 บรรทัด")
    entry.grid(row=1, column=1, sticky='w', pady=5, padx=10)
    
    ttk.Button(basic_frame, text="กดเพื่อดึงค่า", command=lambda: messagebox.showinfo("Info", f"คุณพิมพ์ว่า: {entry.get()}")).grid(row=1, column=2, padx=10, pady=5)

    text_frame = ttk.LabelFrame(tab1, text=" Text & Scrollbar (ข้อความยาวๆ) ", padding=10)
    text_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))
    
    text_widget = tk.Text(text_frame, height=10, wrap='word', bg=WHITE, relief="flat", highlightbackground=BORDER, highlightthickness=1)
    text_widget.pack(side='left', fill='both', expand=True)
    text_widget.insert('1.0', "Text Widget สำหรับข้อความหลายบรรทัด\nทดสอบ Scrollbar กับธีมสีขาว...\n" * 15)
    
    scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=text_widget.yview)
    scrollbar.pack(side='right', fill='y')
    text_widget.configure(yscrollcommand=scrollbar.set)

    # ==========================================
    # Tab 2: Selections 
    # ==========================================
    select_frame = ttk.LabelFrame(tab2, text=" ตัวเลือกแบบต่างๆ ", padding=20)
    select_frame.pack(fill='both', expand=True, padx=20, pady=20)
    
    ttk.Label(select_frame, text="Combobox (Dropdown):", style='White.TLabel').grid(row=0, column=0, sticky='w', pady=10)
    combo = ttk.Combobox(select_frame, values=["ตัวเลือกที่ 1", "ตัวเลือกที่ 2", "ตัวเลือกที่ 3"], state="readonly", width=25)
    combo.current(0)
    combo.grid(row=0, column=1, sticky='w', pady=10, padx=10)
    
    ttk.Label(select_frame, text="Checkbutton:", style='White.TLabel').grid(row=1, column=0, sticky='w', pady=10)
    check_var1 = tk.BooleanVar(value=True)
    check_var2 = tk.BooleanVar(value=False)
    ttk.Checkbutton(select_frame, text="ตัวเลือก A", variable=check_var1, style='White.TCheckbutton').grid(row=1, column=1, sticky='w', padx=10)
    ttk.Checkbutton(select_frame, text="ตัวเลือก B", variable=check_var2, style='White.TCheckbutton').grid(row=1, column=2, sticky='w', padx=10)

    ttk.Label(select_frame, text="Radiobutton:", style='White.TLabel').grid(row=2, column=0, sticky='w', pady=10)
    radio_var = tk.StringVar(value="Option 1")
    ttk.Radiobutton(select_frame, text="ตัวเลือก 1", variable=radio_var, value="Option 1", style='White.TRadiobutton').grid(row=2, column=1, sticky='w', padx=10)
    ttk.Radiobutton(select_frame, text="ตัวเลือก 2", variable=radio_var, value="Option 2", style='White.TRadiobutton').grid(row=2, column=2, sticky='w', padx=10)

    ttk.Label(select_frame, text="Spinbox:", style='White.TLabel').grid(row=3, column=0, sticky='w', pady=10)
    spinbox = ttk.Spinbox(select_frame, from_=0, to=100, width=5)
    spinbox.set(50)
    spinbox.grid(row=3, column=1, sticky='w', pady=10, padx=10)

    ttk.Label(select_frame, text="Scale (Slider):", style='White.TLabel').grid(row=4, column=0, sticky='w', pady=10)
    ttk.Scale(select_frame, from_=0, to=100, orient='horizontal', length=200).grid(row=4, column=1, columnspan=2, sticky='w', padx=10)

    # ==========================================
    # Tab 3: Data & Layouts 
    # ==========================================
    prog_frame = ttk.LabelFrame(tab3, text=" Progressbar ", padding=10)
    prog_frame.pack(fill='x', padx=20, pady=20)
    
    ttk.Label(prog_frame, text="Determinate (ทราบความคืบหน้า):", style='White.TLabel').pack(anchor='w')
    progress1 = ttk.Progressbar(prog_frame, orient='horizontal', length=300, mode='determinate', value=60)
    progress1.pack(anchor='w', pady=5)

    ttk.Label(prog_frame, text="Indeterminate (กำลังประมวลผล):", style='White.TLabel').pack(anchor='w')
    progress2 = ttk.Progressbar(prog_frame, orient='horizontal', length=300, mode='indeterminate')
    progress2.pack(anchor='w', pady=5)
    progress2.start(10)

    paned = ttk.PanedWindow(tab3, orient='horizontal')
    paned.pack(fill='both', expand=True, padx=20, pady=(0, 20))

    # ซ้าย: Listbox
    list_frame = ttk.Frame(paned, style='White.TFrame')
    paned.add(list_frame, weight=1)
    
    ttk.Label(list_frame, text="Listbox (รายการแบบแนวตั้ง):", style='White.TLabel').pack(anchor='w')
    listbox = tk.Listbox(list_frame, height=5, bg=WHITE, relief="flat", highlightbackground=BORDER, highlightthickness=1)
    for item in ["รายการที่ 1", "รายการที่ 2", "รายการที่ 3", "รายการที่ 4", "รายการที่ 5"]:
        listbox.insert(tk.END, item)
    listbox.pack(side='left', fill='both', expand=True)
    
    list_scroll = ttk.Scrollbar(list_frame, orient='vertical', command=listbox.yview)
    list_scroll.pack(side='right', fill='y')
    listbox.config(yscrollcommand=list_scroll.set)

    # ขวา: Treeview
    tree_frame = ttk.Frame(paned, style='White.TFrame')
    paned.add(tree_frame, weight=2)

    ttk.Label(tree_frame, text="Treeview (ใช้ทำตาราง):", style='White.TLabel').pack(anchor='w')
    columns = ("ID", "Name", "Role")
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
    tree.heading("ID", text="รหัส")
    tree.heading("Name", text="ชื่อ")
    tree.heading("Role", text="ตำแหน่ง")
    tree.column("ID", width=80)
    tree.column("Name", width=150)
    tree.column("Role", width=120)
    
    tree.insert("", tk.END, values=("001", "สมชาย", "Admin"))
    tree.insert("", tk.END, values=("002", "สมหญิง", "User"))
    tree.insert("", tk.END, values=("003", "สมศักดิ์", "Guest"))
    tree.pack(side='left', fill='both', expand=True)

    tree_scroll = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
    tree_scroll.pack(side='right', fill='y')
    tree.config(yscrollcommand=tree_scroll.set)

    # ==========================================
    # Tab 4: Advanced & Dialogs 
    # ==========================================
    dialog_frame = ttk.LabelFrame(tab4, text=" ระบบ Dialog (หน้าต่างย่อยของระบบ) ", padding=20)
    dialog_frame.pack(fill='x', padx=20, pady=20)

    def open_custom_popup():
        popup = tk.Toplevel(root)
        popup.title("หน้าต่าง Custom Popup")
        popup.geometry("300x150")
        popup.configure(bg=BG_COLOR)
        popup.transient(root)
        ttk.Label(popup, text="นี่คือหน้าต่าง Toplevel\nคุณสามารถใส่ UI อะไรลงไปในนี้ก็ได้").pack(pady=20)
        ttk.Button(popup, text="ปิดหน้าต่าง", command=popup.destroy).pack()

    ttk.Button(dialog_frame, text="เปิดหน้าต่างเลือกไฟล์", command=lambda: filedialog.askopenfilename()).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(dialog_frame, text="เปิดหน้าต่างเลือกสี", command=lambda: colorchooser.askcolor()).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(dialog_frame, text="สร้างหน้าต่าง Pop-up", command=open_custom_popup).grid(row=0, column=2, padx=5, pady=5)

    canvas_frame = ttk.LabelFrame(tab4, text=" Canvas (พื้นที่สำหรับวาดรูป) ", padding=10)
    canvas_frame.pack(fill='x', padx=20, pady=10)
    
    canvas = tk.Canvas(canvas_frame, bg="#FAFAFA", height=150, highlightthickness=0)
    canvas.pack(fill='x')
    canvas.create_rectangle(20, 20, 100, 100, fill="lightblue", outline="blue", width=2)
    canvas.create_oval(150, 20, 230, 100, fill="lightgreen", outline="green", width=2)
    canvas.create_line(300, 20, 400, 100, fill="red", width=3)
    canvas.create_text(500, 60, text="สามารถวาดรูปทรง หรือใส่รูปลง Canvas ได้!", font=("Tahoma", 12, "bold"), fill="purple")

    context_frame = ttk.LabelFrame(tab4, text=" Context Menu (ลองคลิกขวาที่ป้ายสีเหลืองด้านล่าง) ", padding=10)
    context_frame.pack(fill='x', padx=20, pady=10)

    right_click_label = tk.Label(context_frame, text=">> คลิกขวาที่นี่ <<", bg="#FFF59D", fg=TEXT_COLOR, width=30, height=3)
    right_click_label.pack(pady=10)

    rc_menu = tk.Menu(root, tearoff=0)
    rc_menu.add_command(label="คัดลอก (Copy)", command=lambda: messagebox.showinfo("Action", "กดคัดลอกแล้ว"))
    rc_menu.add_command(label="วาง (Paste)", command=lambda: messagebox.showinfo("Action", "กดวางแล้ว"))
    
    def show_context_menu(event):
        rc_menu.tk_popup(event.x_root, event.y_root)

    right_click_label.bind("<Button-3>", show_context_menu)

    # ==========================================
    # Tab 5: Extras & Scroll Frame 
    # ==========================================
    extra_frame = ttk.LabelFrame(tab5, text=" วิดเจ็ตเพิ่มเติม (Separator, Message, OptionMenu) ", padding=10)
    extra_frame.pack(fill='x', padx=20, pady=20)

    ttk.Label(extra_frame, text="1. tk.Message:", style='White.TLabel').grid(row=0, column=0, sticky='nw')
    msg = tk.Message(extra_frame, text="นี่คือ Message widget มันใช้สำหรับข้อความยาวๆ โดยมันจะทำการปัดบรรทัดให้เราอัตโนมัติตามความกว้างที่เรากำหนดไว้", width=400, bg=WHITE, fg=TEXT_COLOR)
    msg.grid(row=0, column=1, sticky='w', pady=5)

    ttk.Separator(extra_frame, orient='horizontal').grid(row=1, column=0, columnspan=2, sticky='ew', pady=10)

    ttk.Label(extra_frame, text="2. tk.OptionMenu:", style='White.TLabel').grid(row=2, column=0, sticky='w')
    option_var = tk.StringVar(value="เลือกข้อมูล")
    option_menu = tk.OptionMenu(extra_frame, option_var, "ตัวเลือก 1", "ตัวเลือก 2", "ตัวเลือก 3")
    option_menu.configure(bg=WHITE, relief="solid", borderwidth=1, highlightthickness=0)
    option_menu.grid(row=2, column=1, sticky='w', pady=5)

    scroll_outer_frame = ttk.LabelFrame(tab5, text=" เทคนิคขั้นสูง: Frame ที่มีแถบเลื่อน (Scrollable Frame) ", padding=10)
    scroll_outer_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))
    
    canvas_scroll = tk.Canvas(scroll_outer_frame, bg=WHITE, highlightthickness=0)
    scrollbar_v = ttk.Scrollbar(scroll_outer_frame, orient="vertical", command=canvas_scroll.yview)
    scrollable_inner_frame = ttk.Frame(canvas_scroll, style='White.TFrame')
    
    scrollable_inner_frame.bind("<Configure>", lambda e: canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all")))
    canvas_scroll.create_window((0, 0), window=scrollable_inner_frame, anchor="nw")
    canvas_scroll.configure(yscrollcommand=scrollbar_v.set)
    
    canvas_scroll.pack(side="left", fill="both", expand=True)
    scrollbar_v.pack(side="right", fill="y")
    
    for i in range(1, 21):
        tk.Label(scrollable_inner_frame, text=f"ฟอร์มข้อมูลแถวที่ {i}:", bg=WHITE, fg=TEXT_COLOR).grid(row=i, column=0, padx=10, pady=5, sticky='w')
        ttk.Entry(scrollable_inner_frame, width=30).grid(row=i, column=1, padx=10, pady=5)
        ttk.Button(scrollable_inner_frame, text="บันทึก").grid(row=i, column=2, padx=10, pady=5)

    # ==========================================
    # Tab 6: Dashboard
    # ==========================================
    dash_bg = tk.Frame(tab6, bg=BG_COLOR)
    dash_bg.pack(fill='both', expand=True)
    
    dash_container = tk.Frame(dash_bg, bg=BG_COLOR)
    dash_container.pack(fill='both', expand=True, padx=30, pady=30)

    tk.Label(dash_container, text="ภาพรวมระบบ (System Overview)", font=("Tahoma", 18, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor='w', pady=(0, 20))

    cards_frame = tk.Frame(dash_container, bg=BG_COLOR)
    cards_frame.pack(fill='x')

    def create_kpi_card(parent, title, value, color):
        card = tk.Frame(parent, bg=WHITE, highlightbackground=BORDER, highlightthickness=1)
        card.pack(side='left', fill='both', expand=True, padx=(0, 20))
        
        color_bar = tk.Frame(card, bg=color, height=5)
        color_bar.pack(fill='x', side='top')
        
        tk.Label(card, text=title, font=("Tahoma", 11), bg=WHITE, fg="#666666").pack(anchor='w', padx=20, pady=(15, 5))
        tk.Label(card, text=value, font=("Tahoma", 24, "bold"), bg=WHITE, fg=TEXT_COLOR).pack(anchor='w', padx=20, pady=(0, 20))

    create_kpi_card(cards_frame, "ผู้ใช้งานปัจจุบัน", "1,204", "#4CAF50")
    create_kpi_card(cards_frame, "ยอดขายวันนี้", "฿ 45,900", "#2196F3")
    create_kpi_card(cards_frame, "สถานะระบบ", "ปกติ (Online)", "#9C27B0")
    create_kpi_card(cards_frame, "การแจ้งเตือน", "3 รายการ", "#FF9800")

    content_frame = tk.Frame(dash_container, bg=BG_COLOR)
    content_frame.pack(fill='both', expand=True, pady=(20, 0))

    left_card = tk.Frame(content_frame, bg=WHITE, highlightbackground=BORDER, highlightthickness=1)
    left_card.pack(side='left', fill='both', expand=True, padx=(0, 20))
    
    tk.Label(left_card, text="รายการธุรกรรมล่าสุด", font=windows_font_bold, bg=WHITE, fg=TEXT_COLOR).pack(anchor='w', padx=20, pady=15)
    ttk.Separator(left_card, orient='horizontal').pack(fill='x', padx=20)
    
    dash_tree = ttk.Treeview(left_card, columns=("Time", "Action", "Status"), show='headings', height=8)
    dash_tree.heading("Time", text="เวลา")
    dash_tree.heading("Action", text="กิจกรรม")
    dash_tree.heading("Status", text="สถานะ")
    dash_tree.column("Time", width=100)
    dash_tree.column("Action", width=250)
    dash_tree.column("Status", width=100)
    
    mock_data = [("14:30", "ผู้ใช้ #102 สมัครสมาชิก", "สำเร็จ"), 
                 ("14:15", "ชำระเงินรหัส #A928", "สำเร็จ"), 
                 ("13:50", "พยายามเข้าสู่ระบบผิดพลาด", "ล้มเหลว")]
    for item in mock_data:
        dash_tree.insert("", tk.END, values=item)
    dash_tree.pack(fill='both', expand=True, padx=20, pady=15)

    right_card = tk.Frame(content_frame, bg=WHITE, highlightbackground=BORDER, highlightthickness=1, width=300)
    right_card.pack(side='right', fill='y')
    right_card.pack_propagate(False)
    
    tk.Label(right_card, text="การจัดการด่วน", font=windows_font_bold, bg=WHITE, fg=TEXT_COLOR).pack(anchor='w', padx=20, pady=15)
    ttk.Separator(right_card, orient='horizontal').pack(fill='x', padx=20)
    
    action_frame = tk.Frame(right_card, bg=WHITE)
    action_frame.pack(fill='both', expand=True, padx=20, pady=15)
    
    ttk.Button(action_frame, text="สร้างรายงาน (Generate Report)").pack(fill='x', pady=5, ipady=5)
    ttk.Button(action_frame, text="เพิ่มผู้ใช้ใหม่ (Add User)").pack(fill='x', pady=5, ipady=5)
    ttk.Button(action_frame, text="ตั้งค่าระบบ (Settings)").pack(fill='x', pady=5, ipady=5)
    ttk.Button(action_frame, text="รีเฟรชข้อมูล (Refresh)").pack(fill='x', pady=5, ipady=5)

    # ==========================================
    # Tab 7: Drag & Drop (Internal)
    # ==========================================
    dnd_frame = ttk.LabelFrame(tab7, text=" การจัดการเมาส์ (Mouse Events: Drag & Drop) ", padding=20)
    dnd_frame.pack(fill='both', expand=True, padx=20, pady=20)

    # คำอธิบายส่วนบน
    desc_text = "Tkinter พื้นฐานไม่มี Widget สำหรับรับการลากไฟล์จากภายนอก แต่เราสามารถใช้คำสั่ง .bind() เพื่อตรวจจับเมาส์ และสร้างระบบลาก UI ภายในหน้าต่างได้อย่างอิสระ ลองนำเมาส์ไปลากกล่องสีสันด้านล่างดูครับ"
    tk.Message(dnd_frame, text=desc_text, width=800, bg=WHITE, fg=TEXT_COLOR, font=windows_font).pack(anchor='w', pady=(0, 10))

    # พื้นที่สำหรับทดสอบการลาก (Drag Area)
    drag_area = tk.Frame(dnd_frame, bg="#E0E0E0", highlightbackground=BORDER, highlightthickness=1)
    drag_area.pack(fill='both', expand=True, pady=10)
    
    # คำสั่งบังคับไม่ให้ Frame หดตัวตามเนื้อหาที่อยู่ข้างใน (จำเป็นเมื่อใช้คำสั่ง .place() ในการจัดการตำแหน่ง)
    drag_area.pack_propagate(False) 

    # --- ฟังก์ชันควบคุมการลาก ---
    def on_drag_start(event):
        """เริ่มบันทึกพิกัดเมื่อกดคลิกซ้ายค้างที่วิดเจ็ต"""
        widget = event.widget
        # บันทึกพิกัด (X, Y) ที่เมาส์ชี้เทียบกับมุมซ้ายบนของวิดเจ็ตนั้น
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y
        # สั่งให้วิดเจ็ตที่กำลังจับอยู่ ลอยขึ้นมาอยู่หน้าสุด
        widget.lift()

    def on_drag_motion(event):
        """อัปเดตตำแหน่งวิดเจ็ตตามการลากเมาส์"""
        widget = event.widget
        # คำนวณพิกัด X, Y สัมบูรณ์ใหม่เทียบกับ Frame (drag_area) ที่มันอยู่
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        # ย้ายตำแหน่งไปยังพิกัดใหม่
        widget.place(x=x, y=y)

    # --- สร้างวิดเจ็ตที่สามารถลากได้ ---
    # กล่องที่ 1
    draggable_box1 = tk.Label(drag_area, text="ลากฉันสิ (Box 1)", bg="#2196F3", fg="white", font=windows_font_bold, padx=30, pady=20, cursor="fleur")
    draggable_box1.place(x=50, y=50) # ใช้ place() เพื่อให้พิกัดเป็นอิสระ
    draggable_box1.bind("<ButtonPress-1>", on_drag_start) # ผูกเหตุการณ์คลิก
    draggable_box1.bind("<B1-Motion>", on_drag_motion)    # ผูกเหตุการณ์ลาก

    # กล่องที่ 2
    draggable_box2 = tk.Label(drag_area, text="จับฉันลากเลย (Box 2)", bg="#FF9800", fg="white", font=windows_font_bold, padx=30, pady=20, cursor="fleur")
    draggable_box2.place(x=300, y=150)
    draggable_box2.bind("<ButtonPress-1>", on_drag_start)
    draggable_box2.bind("<B1-Motion>", on_drag_motion)
    
    # กล่องที่ 3
    draggable_box3 = tk.Label(drag_area, text="ลากมาชนกันได้นะ (Box 3)", bg="#9C27B0", fg="white", font=windows_font_bold, padx=30, pady=20, cursor="fleur")
    draggable_box3.place(x=150, y=300)
    draggable_box3.bind("<ButtonPress-1>", on_drag_start)
    draggable_box3.bind("<B1-Motion>", on_drag_motion)

    # ==========================================
    # ส่วนล่างสุด
    # ==========================================
    bottom_frame = tk.Frame(root, bg=BG_COLOR)
    bottom_frame.pack(fill='x', side='bottom', padx=20, pady=15)

    tk.Label(bottom_frame, text="เวอร์ชัน 1.0.0 | โหมด White-Gray UI (Full Collection)", bg=BG_COLOR, fg="#888888").pack(side='left')

    exit_btn = ttk.Button(bottom_frame, text="ออกจากโปรแกรม (Close)", command=quit_app)
    exit_btn.pack(side='right', ipadx=20, ipady=5)

    root.mainloop()

if __name__ == "__main__":
    create_showcase()