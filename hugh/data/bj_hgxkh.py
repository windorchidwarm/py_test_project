# 班教合规性考核
import pandas as pd
import openpyxl
import numpy as  np
import os

#结果存放目录


base_path = os.path.dirname(os.path.realpath(__file__))\
    .replace(os.path.join('hugh', 'data'), '')
print(base_path)
file_dir = os.path.join(os.path.join(base_path, 'files'), 'data')
# output_file = 'F:/cyt/kettle/【班教】集团教务合规性考核/结果数据'
output_file = os.path.join(file_dir, '结果数据')
# 读取基础数据
df_class = pd.DataFrame(pd.read_excel(os.path.join(file_dir, '一体化班级查询基础数据.xlsx'),sheet_name = 'Sheet1', encoding='gbk', nrows=100))

# 1-0人班处理
df_01 =  df_class[
    (~df_class['班级名称（外）'].str.contains('取消')) &
    (df_class['当前人数(占名额)'] == 0)
]

# 2-网课班级
df_02 =  df_class[
    (~df_class['班级名称（外）'].str.contains('取消')) &  (~df_class['产品体系'].isin(['计费体系'])) &
    (df_class['当前人数(占名额)'] == 0)
]

#18-非本部门项目
# 筛选出班级名称不含取消；非计费体系
# 标准部门为少儿部、中学班课部、中学小组课部
df_18 = df_class [( ~df_class['班级名称（外）'].str.contains('取消')) &  (~df_class['产品体系'].isin(['计费体系'])) &
            (
                ( (df_class['标准部门'].isin(['少儿部','中学班课部','中学小组课部','中学一对一部'])) &
                  (df_class['班级名称（外）'].str.contains('托福|雅思|TOEFL|ISEE|IELTS|考研|四级|六级'))) |
                ( (df_class['标准部门'].isin(['国内大学部','国外考试部','英语学习部'])) &
                  (df_class['班级名称（外）'].str.contains('中学|少儿|小学|中考|高考|初一|初二|高一|高二|年级')))
            )
        ]

#输出获取数据条数
#返回列数：df.shape[1]
# 返回行数：len(df) 或者 df.shape[0]


# df_12.to_excel('F:/cyt/kettle/【班教】集团教务合规性考核/结果数据/合规性考核【班教】.xlsx' ,sheet_name='12-非本部门项目',index = False)



# 19-对内外科目年级
# 列包含列 df_test  = df_class[df_class.apply(lambda x: str(x['科目(内)']) in x['班级名称（外）'], axis=1)]
#df = df[df.apply(lambda x: str(x['id']) in x['class'], axis=1)]
# axis 是维度轴 =1 是行计算； =0是列结算
# 这个的意思是在df中用apply函数 x代表一行数据；返回的是id这个字段的str型是否包含在class中的布尔值
df_19 = df_class [( ~df_class['班级名称（外）'].str.contains('取消|全科')) &  (~df_class['产品体系'].isin(['计费体系'])) &
                  ((df_class['标准部门'].isin(['少儿部', '中学班课部', '中学小组课部'])) & (
                      (~ df_class.apply(lambda x: str(x['科目(内)']) in x['班级名称（外）'], axis=1)  ) |
                      (~ df_class.apply(lambda x: str(x['年级序数']) in x['班级名称（内）'], axis=1)  )
                       )
                   )
                  ]

# df_13.to_excel('F:/cyt/kettle/【班教】集团教务合规性考核/结果数据/合规性考核【班教】.xlsx' ,sheet_name='13-对内外科目年级',index = False)

#20-功能型班级
df_20 = df_class[( ~df_class['班级名称（外）'].str.contains('取消')) &
                 (~df_class['产品体系'].isin(['计费体系','专项体系']))  &
                 (df_class['班级名称（外）'].str.contains('活动|辅导|督导|赠送|自习|定金|订金|预收|引流|费|礼品')) ]

#21-学费0
df_21 = df_class[( ~df_class['班级名称（外）'].str.contains('取消')) &
                 (~df_class['产品体系'].isin(['计费体系']))  &
                 (~df_class['班级名称（外）'].str.contains('活动|辅导|督导|赠送|自习')) &
                 (df_class['班级标价'] == 0)]

#22-课时0
#班级课次时长是财务结转表内的字段
# 一体化班级查询内无该字段，此条合规性换成【班级课次数】
df_22 = df_class[( ~df_class['班级名称（外）'].str.contains('取消|订金|定金|预收|引流')) &
                 (~df_class['产品体系'].isin(['计费体系']))  &
                 (df_class['班级课次数'] == 0)]

#23-关联班号

df_23 = df_class[( ~df_class['班级名称（外）'].str.contains('取消')) &
                 (df_class['标准部门'].isin(['少儿部', '中学班课部', '中学小组课部', '中学一对一部'])) &
                 (~df_class['产品体系'].isin(['计费体系']) ) &(
                 ( (df_class['关联班号'].isnull() ) & (df_class['季度'].str.contains('春季上|春季下|秋季上|秋季下')) ) |
                 ( (~df_class['关联班号'].isnull() ) & (df_class['季度'].isin(['暑假','秋季','寒假','春季'])) ) |
                 ( (~df_class['关联班号'].isnull() ) &
                   (df_class['标准部门'].isin([ '中学班课部', '中学小组课部', '中学一对一部'])) &
                   ((df_class['班级编码'].str.endswith('A',na=False))
                    | (df_class['班级编码'].str.endswith('B',na=False)) ) ) |
                 ( (~df_class['关联班号'].isnull() ) &
                   (df_class['标准部门'].isin(['少儿部'])) &
                   ((df_class['班级编码'].str.endswith('1',na=False))  | (df_class['班级编码'].str.endswith('2',na=False)) ) )
                )]

#24-班级类型
df_24 = df_class[( ~df_class['班级名称（外）'].str.contains('取消|全科')) &
                 (~df_class['产品体系'].isin(['计费体系']))  &
                 (df_class['标准部门'].isin(['少儿部', '中学班课部', '中学小组课部'])) & (
                     ( ((df_class['科目(外)'].isin(['英语','数学','语文','物理','化学','生物','地理','政治','历史','科学'])) &
                      (~df_class.apply(lambda x: str(x['科目(外)']) in x['班级类型'], axis=1) )) ) |
                     ((df_class['科目(外)'].isin('科学')) & (~df_class['班级类型'].isin(['初一物理','初二化学','小升初衔接物理'])))
                 )]

#25-住宿标志
df_25 = df_class[( ~df_class['班级名称（外）'].str.contains('取消')) &
                 (~df_class['产品体系'].isin(['计费体系']))  &
                 (df_class['班级名称（外）'].str.contains('住宿|营')) &
                 (~df_class['上课形式'].str.contains('住宿', na=False))]

#26-班级状态
df_26 = df_class[(df_class['班级状态'].isin(['修改待审核','取消待审核']))]

#27-主带课教师空
df_27 = df_class[( ~df_class['班级名称（外）'].str.contains('取消')) &
                 (~df_class['产品体系'].isin(['计费体系']))  &
                 (df_class['标准部门'].isin(['少儿部', '中学班课部', '中学小组课部', '中学一对一部'])) &
                 (df_class['标准人数'] >= 6) &
                 (df_class['续班类型'].isin(['可续','连季续','隔季续']))  &
                 (df_class['主带课老师'].isnull())
                 ]



#在一个excel当中写入多个sheet
# 这里需要提前安装openpyxl 库
excel_writer = pd.ExcelWriter('F:/cyt/kettle/【班教】集团教务合规性考核/结果数据/合规性考核【班教】.xlsx')  # 定义writer，选择文件（文件可以不存在）

df_01.to_excel(excel_writer, sheet_name='1-0人班处理', index=False)  # 写入指定表单
df_18.to_excel(excel_writer, sheet_name='18-非本部门项目', index=False)  # 写入指定表单
df_19.to_excel(excel_writer, sheet_name='19-对内外科目年级', index=False)  # 写入指定表单
df_20.to_excel(excel_writer, sheet_name='20-功能型班级', index=False)  # 写入指定表单
df_21.to_excel(excel_writer, sheet_name='21-学费0', index=False)  # 写入指定表单
df_22.to_excel(excel_writer, sheet_name='22-课时0', index=False)  # 写入指定表单
df_23.to_excel(excel_writer, sheet_name='23-关联班号', index=False)  # 写入指定表单
df_24.to_excel(excel_writer, sheet_name='24-班级类型', index=False)  # 写入指定表单
df_25.to_excel(excel_writer, sheet_name='25-住宿标志', index=False)  # 写入指定表单
df_26.to_excel(excel_writer, sheet_name='26-班级状态', index=False)  # 写入指定表单
df_27.to_excel(excel_writer, sheet_name='27-主带课教师空', index=False)  # 写入指定表单

excel_writer.save()  # 储存文件
excel_writer.close()  # 关闭writer