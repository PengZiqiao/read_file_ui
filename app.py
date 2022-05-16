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
        names = ['当前期数',
                 '应还款日期',
                 '应还本金',
                 '应还利息',
                 '应还罚息',
                 '应还其他费项',
                 '实还本金',
                 '实还利息',
                 '实还罚息',
                 '实还其他费项',
                 '实还日期']
    elif 'REPAY' in file.filename:
        names = ['还款类别',
                 '还款期数',
                 '还款请求流水号',
                 '还款总金额',
                 '还款日期',
                 '还款本金（客户账）',
                 '还款利息（客户账）',
                 '还款罚息（客户账）',
                 '还款其他费用（客户账）']

    table = pd.read_csv(file, sep='|', names=names, dtype=str)
    table.fillna('', inplace=True)

    return jsonify({
        'tableColumns': table.columns.tolist(),
        'tableData': table.to_dict(orient='records')
    })

# from flaskwebgui import FlaskUI
# ui = FlaskUI(app)
# ui.run()
