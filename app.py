import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transfer', methods=['POST'])
def transfer():
    file = request.files.get('file')

    if 'PLAN' in file.filename:
        names = ['360放款请求流水号',
                 '当前期数',
                 '应还款日期',
                 '应还本金',
                 '应还利息',
                 '应还罚息',
                 '应还其他费项',
                 '实还本金',
                 '实还利息',
                 '实还罚息',
                 '实还其他费项',
                 '实还日期',
                 '开始日期',
                 '状态',
                 '营销减免金额（即还款明细文件中的红线减免金额）',
                 '红线减免金额（即还款明细文件中的营销减免金额）']
    elif 'REPAY' in file.filename:
        names = ['放款请求流水号',
                 '请求方代码',
                 '还款类别',
                 '还款期数',
                 '还款请求流水号',
                 '还款总金额',
                 '还款日期',
                 '还款本金（客户账）',
                 '还款利息（客户账）',
                 '还款罚息（客户账）',
                 '还款其他费用（客户账）',
                 '红线减免金额',
                 '360活动减免金额',
                 '360侧应收分润费',
                 '代扣渠道',
                 '代扣申请流水号',
                 '当期是否结清',
                 '拆分利息',
                 '拆分提前还款违约金']

    table = pd.read_csv(file, sep='|', names=names, dtype=str)
    table.fillna('', inplace=True)

    return jsonify({
        'tableColumns': table.columns.tolist(),
        'tableData': table.to_dict(orient='records')
    })

# from flaskwebgui import FlaskUI
# ui = FlaskUI(app)
# ui.run()
