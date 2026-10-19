import pandas as pd
import matplotlib.pyplot as plt

# 1. قراءة البيانات (تأكدي أن اسم الملف مطابق لملفك)
# استخدمنا السطر الثاني كعناوين للأعمدة لأن السطر الأول يحتوي على فراغات كثيرة
df = pd.read_csv('sales_data.csv', header=1)

# 2. استخراج بيانات المنتجات فقط (تصفية البيانات)
product_data = df[df['section'] == 'Product'].copy()

# تحويل القيم إلى أرقام لتجنب أي مشاكل في الرسم
product_data['value1'] = pd.to_numeric(product_data['value1'])

# ترتيب المنتجات من الأعلى مبيعاً إلى الأقل
product_data = product_data.sort_values(by='value1', ascending=True)

# 3. رسم البياني (مخطط شريطي أفقي لمبيعات المنتجات)
plt.figure(figsize=(10, 6))
bars = plt.barh(product_data['label'], product_data['value1'], color='#1f77b4')

# إضافة العناوين وتنسيق الشكل
plt.title('إجمالي مبيعات المنتجات ($)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('المبيعات بالدولار', fontsize=12)
plt.ylabel('اسم المنتج', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)

# إضافة أرقام المبيعات فوق كل عمود بشكل منسق
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f' ${width:,.0f}', 
             va='center', ha='left', fontsize=10, fontweight='bold')

plt.tight_layout()

# 4. حفظ الرسم البياني كصورة بجودة عالية
plt.savefig('sales_chart.png', dpi=300)
print("✅ تم استخراج البيانات ورسم المخطط وحفظ الصورة بنجاح باسم 'sales_chart.png'!")
