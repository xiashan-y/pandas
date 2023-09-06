from flask import Flask, request, render_template

app = Flask(__name__)

# 使用字典来关联证件号与账号和密码
data = {
    "340403201204150423": {"姓名": "宋馨雨", "账号": 43204, "密码": "cd12345678"},
    "AM090698": {"姓名": "赵嘉西", "账号": 43177, "密码": "cd12345678"},
    "310114201206064825": {"姓名": "陈楚君", "账号": 43178, "密码": "cd12345678"},
    "231282201207260046": {"姓名": "陈欣霖", "账号": 43179, "密码": "cd12345678"},
    "310113201103291949": {"姓名": "陈伊煊", "账号": 43180, "密码": "cd12345678"},
    "310106201212100853": {"姓名": "陈喆涵", "账号": 43181, "密码": "cd12345678"},
    "310106201008204049": {"姓名": "崔昕恬", "账号": 43183, "密码": "cd12345678"},
    "310105201212313617": {"姓名": "崔奕辰", "账号": 43402, "密码": "cd12345678"},
    "320482201408200121": {"姓名": "范文瑾", "账号": 43184, "密码": "cd12345678"},
    "320413201606060040": {"姓名": "范欣瑜", "账号": 43404, "密码": "cd12345678"},
    "310107201206127861": {"姓名": "方涵", "账号": 43405, "密码": "cd12345678"},
    "310115201401151832": {"姓名": "方闳毅", "账号": 43186, "密码": "cd12345678"},
    "810000201210060098": {"姓名": "古将君", "账号": 43185, "密码": "cd12345678"},
    "320585201407290027": {"姓名": "顾希颜", "账号": 43188, "密码": "cd12345678"},
    "310230201401305167": {"姓名": "韩昕言", "账号": 43190, "密码": "cd12345678"},
    "310101201508064255": {"姓名": "侯城宇", "账号": 43191, "密码": "cd12345678"},
    "310110201307255625": {"姓名": "金芯丞", "账号": 43193, "密码": "cd12345678"},
    "310107201311040426": {"姓名": "李一禾", "账号": 43195, "密码": "cd12345678"},
    "33010420141016420X": {"姓名": "陆一菲", "账号": 43196, "密码": "cd12345678"},
    "310107201201194942": {"姓名": "陆怡宁", "账号": 43200, "密码": "cd12345678"},
    "310107201411213435": {"姓名": "马诚远", "账号": 43406, "密码": "cd12345678"},
    "310106201504085923": {"姓名": "马小雅", "账号": 43407, "密码": "cd12345678"},
    "31011520130915212X": {"姓名": "沈心知", "账号": 43187, "密码": "cd12345678"},
    "310115201307301021": {"姓名": "沈彦舟", "账号": 43189, "密码": "cd12345678"},
    "310115201201182490": {"姓名": "汪宇涛", "账号": 43192, "密码": "cd12345678"},
    "310107201401080413": {"姓名": "王麒源", "账号": 43194, "密码": "cd12345678"},
    "310115201408262463": {"姓名": "温宇歆", "账号": 43408, "密码": "cd12345678"},
    "310113201303023412": {"姓名": "肖锦翔", "账号": 43197, "密码": "cd12345678"},
    "310115201205180740": {"姓名": "严夏", "账号": 43198, "密码": "cd12345678"},
    "310104201208270814": {"姓名": "姚岩霖", "账号": 43199, "密码": "cd12345678"},
    "310104201507083648": {"姓名": "张纾菡", "账号": 43201, "密码": "cd12345678"},
    "330102201208213044": {"姓名": "张宜", "账号": 43202, "密码": "cd12345678"},
    "310110201312040565": {"姓名": "张梓筠", "账号": 43203, "密码": "cd12345678"},
    "340403201204150423": {"姓名": "宋馨雨", "账号": 43204, "密码": "cd12345678"},
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        camper_id = request.form.get("camper_id")
        if camper_id:
            # 查找证件号对应的账号和密码
            camper_info = data.get(camper_id)
            if camper_info:
                account = camper_info["账号"]
                password = camper_info["密码"]
                yy_name = camper_info["姓名"]
                return f"营员姓名：{yy_name} 证件号：{camper_id}<br>志愿者登陆ID：{account}<br>密码：{password}<br><a href='/'>返回</a>"
            else:
                return "证件号不存在请确认后重试<br><a href='/'>返回</a>"
        else:
            return "请输入证件号"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
