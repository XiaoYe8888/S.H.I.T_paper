import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题



# 数据1：学生焦虑得分对比（正常开学 vs 提前开学）
data_anxiety = pd.DataFrame({
    '组别': ['正常开学', '正常开学', '提前开学', '提前开学'],
    '学段': ['初中', '高中', '初中', '高中'],
    '焦虑得分均值': [40.21, 44.52, 55.67, 62.47]
})

# 数据2：学生睡眠时长变化（假期 vs 提前开学后）
data_sleep = pd.DataFrame({
    '时间节点': ['假期中', '开学前1周', '开学后1周'],
    '日均睡眠时长(小时)': [8.72, 6.15, 7.02]
})

# 数据3：不同家庭结构家长对提前开学的支持率
data_parents = pd.DataFrame({
    '家庭结构': ['双职工家庭', '全职家长家庭', '留守儿童家庭'],
    '支持率(%)': [78.65, 32.47, 81.24]
})

# 数据4：教师职业倦怠得分对比
data_teacher = pd.DataFrame({
    '组别': ['正常开学筹备期', '提前开学筹备期'],
    '职业倦怠得分均值': [45.21, 62.38]
})



# --- 图1：学生焦虑得分对比（柱状图）---
plt.figure(figsize=(10, 6))
sns.barplot(x='学段', y='焦虑得分均值', hue='组别', data=data_anxiety, palette='viridis')
plt.title('图1 正常开学与提前开学学生焦虑得分均值对比', fontsize=14, fontweight='bold')
plt.ylabel('焦虑自评量表(SAS)得分', fontsize=12)
plt.ylim(30, 70)  # 设置y轴范围，让差异更明显
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('图1_学生焦虑对比.png', dpi=300)  # 保存高清图
plt.show()

# --- 图2：学生睡眠时长变化（折线图）---
plt.figure(figsize=(10, 6))
sns.lineplot(x='时间节点', y='日均睡眠时长(小时)', data=data_sleep, marker='o', linewidth=3, color='coral')
plt.title('图2 学生日均睡眠时长变化趋势', fontsize=14, fontweight='bold')
plt.ylabel('日均睡眠时长(小时)', fontsize=12)
plt.ylim(5, 10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('图2_睡眠时长变化.png', dpi=300)
plt.show()

# --- 图3：不同家庭结构家长支持率（饼图）---
plt.figure(figsize=(8, 8))
colors = ['#66b3ff', '#99ff99', '#ffcc99']
plt.pie(data_parents['支持率(%)'], labels=data_parents['家庭结构'], autopct='%1.1f%%',
        colors=colors, startangle=90, textprops={'fontsize': 12})
plt.title('图3 不同家庭结构对提前开学的支持率', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('图3_家长支持率.png', dpi=300)
plt.show()

# --- 图4：教师职业倦怠得分对比（简单柱状图）---
plt.figure(figsize=(8, 6))
sns.barplot(x='组别', y='职业倦怠得分均值', data=data_teacher, palette='Set2')
plt.title('图4 教师职业倦怠得分均值对比', fontsize=14, fontweight='bold')
plt.ylabel('职业倦怠量表(MBI)得分', fontsize=12)
plt.ylim(30, 75)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('图4_教师职业倦怠.png', dpi=300)
plt.show()