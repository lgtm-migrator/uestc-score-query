import uestc_query
import os

username = os.getenv("TUSERNAME")
password = os.getenv("TPASSWORD")

def test_uestc_parse_all_grades_page():
    table = uestc_query.parse_all_grades_page(all_grades_page_sample) 
    assert len(table) > 0

def test_uestc_score_query():
  res = uestc_query.query(username,password);
  assert res != None
  assert len(res) > 0

all_grades_page_sample = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr">
<head>
  <title></title>
  <meta http-equiv="content-type" content="text/html;charset=utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta http-equiv="pragma" content="no-cache"/>
  <meta http-equiv="cache-control" content="no-cache"/>
  <meta http-equiv="expires" content="0"/>
  <meta http-equiv="content-style-type" content="text/css"/>
  <meta http-equiv="content-script-type" content="text/javascript"/>
  <script>
      window.$BG_LANG='zh';
  </script>
  <script type="text/javascript" src="/eams/static/scripts/jquery/jquery,jquery.ui.core.js?bg=3.4.15"></script>
  <script type="text/javascript" src="/eams/static/scripts/plugins/jquery-form,jquery-history,jquery-colorbox,jquery-chosen.js?bg=3.4.15"></script>
  <script type="text/javascript" src="/eams/static/js/plugins/jquery.subscribe,/js/struts2/jquery.struts2,jquery.ui.struts2.js?bg=3.4.15"></script>
  <script type="text/javascript" src="/eams/static/scripts/beangle/beangle,beangle-ui.js?bg=3.4.15"></script>
  <script type="text/javascript">var App = {contextPath:"/eams"};jQuery(document).ready(function () {jQuery.struts2_jquery.version="3.6.1";beangle.contextPath=App.contextPath;jQuery.scriptPath = App.contextPath+"/static/";jQuery.struts2_jquerySuffix = "";jQuery.ajaxSettings.traditional = true;jQuery.ajaxSetup ({cache: false});});</script>
  <script type="text/javascript" src="/eams/static/scripts/my97/WdatePicker-4.72.js?compress=no"></script>
  <link id="jquery_theme_link" rel="stylesheet" href="/eams/static/themes/smoothness/jquery-ui.css?s2j=3.7.1" type="text/css"/>
  <link id="beangle_theme_link" href="/eams/static/themes/default/beangle-ui,colorbox,chosen.css" rel="stylesheet" type="text/css" />

</head>
<body>

 
<div  style="margin-top:10px;" class="ajax_container"></div>

<table class="gridtable">
	<thead class="gridhead">
		<tr>
			<th>学年度</th>
			<th>学期</th>
			<th>门数</th>
			<th>总学分</th>
			<th>平均绩点</th>
		</tr>
	</thead>
	<tbody>
					<tr class="griddata-even">
						<td>2015-2016</td>
						<td>1</td>
						<td>9</td>
						<td>21.5</td>
						<td>2.74</td>
					</tr>
					<tr class="griddata-odd">
						<td>2015-2016</td>
						<td>2</td>
						<td>12</td>
						<td>33</td>
						<td>3.43</td>
					</tr>
					<tr class="griddata-even">
						<td>2014-2015</td>
						<td>1</td>
						<td>10</td>
						<td>26</td>
						<td>3.34</td>
					</tr>
					<tr class="griddata-odd">
						<td>2016-2017</td>
						<td>1</td>
						<td>9</td>
						<td>23</td>
						<td>2.93</td>
					</tr>
					<tr class="griddata-even">
						<td>2014-2015</td>
						<td>2</td>
						<td>12</td>
						<td>32</td>
						<td>3.21</td>
					</tr>
				<tr class="griddata-odd">
						<th colSpan="2">在校汇总</th>
						<th>52</th>
						<th>135.5</th>
						<th>3.16</th>
				</tr>
	 	<tr class="griddata-even">
	 		<th colSpan="5" align="right">统计时间:2017-01-28 14:54</th>
		</tr>
	</tbody>
</table>

	<div  style="margin-top:10px;text-align:center;font-weight:bold;" class="ajax_container">成绩列表</div>


 
<div class="grid">


<table id="grid21344342991" class="gridtable">
<thead class="gridhead">


<tr>
<th  width="10%" >学年学期</th>
<th  width="10%" >课程代码</th>
<th  width="10%" >课程序号</th>
<th  width="20%" >课程名称</th>
<th  width="14%" >课程类别</th>
<th  width="9%" >学分</th>
<th  width="9%" >总评成绩</th>
<th  width="9%" >最终</th>
</tr>

</thead>

<tbody id="grid21344342991_data"><tr>		<td>2014-2015 2</td>
		<td>B1300620</td>
		<td>B1300620.08</td>
		<td>高级英语读写</td>
<td>A类语言技能类</td>		<td>2</td>
<td style="">	  			74 
</td><td style="">			74
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>K2226520</td>
		<td>K2226520.01</td>
		<td>综合应用设计 I</td>
<td>实践类核心课程</td>		<td>2</td>
<td style="">	  			90 
</td><td style="">			90
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>B1301320</td>
		<td>B1301320.13</td>
		<td>英国文学与文化</td>
<td>B类人文素养类</td>		<td>2</td>
<td style="">	  			66 
</td><td style="">			66
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>I7600120</td>
		<td>I7600120.02</td>
		<td>信息检索与利用</td>
<td>素质教育选修课（社会科学类）</td>		<td>2</td>
<td style="">	  			83 
</td><td style="">			83
</td>		
</tr><tr>		<td>2015-2016 1</td>
		<td>D1000735</td>
		<td>D1000735.28</td>
		<td>概率论与数理统计</td>
<td>学科通识课程</td>		<td>3.5</td>
<td style="">	  			60 
</td><td style="">			60
</td>		
</tr><tr>		<td>2015-2016 1</td>
		<td>I1600320</td>
		<td>I1600320.01</td>
		<td>政治经济学原理与实践</td>
<td>素质教育选修课（社会科学类）</td>		<td>2</td>
<td style="color:red">	  			45 
</td><td style="color:red">			45
</td>		
</tr><tr>		<td>2016-2017 1</td>
		<td>H2227020</td>
		<td>H2227020.01</td>
		<td>大型机编程工具</td>
<td>本专业选修课</td>		<td>2</td>
<td style="">	  			64 
</td><td style="">			64
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>D1000540</td>
		<td>D1000540.D6</td>
		<td>线性代数与空间解析几何I</td>
<td>学科通识课程</td>		<td>4</td>
<td style="">	  			78 
</td><td style="">			78
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>E2201240</td>
		<td>E2201240.01</td>
		<td>数据库原理及应用</td>
<td>学科基础课程</td>		<td>4</td>
<td style="">	  			85 
</td><td style="">			85
</td>		
</tr><tr>		<td>2016-2017 1</td>
		<td>H2227320</td>
		<td>H2227320.01</td>
		<td>云计算</td>
<td>本专业选修课</td>		<td>2</td>
<td style="">	  			87 
</td><td style="">			87
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>H2201810</td>
		<td>H2201810.01</td>
		<td>新生教育</td>
<td>本专业选修课</td>		<td>1</td>
<td style="">	  			89 
</td><td style="">			89
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>G2225030</td>
		<td>G2225030.02</td>
		<td>大型机操作系统</td>
<td>专业核心课程</td>		<td>3</td>
<td style="">	  			80 
</td><td style="">			80
</td>		
</tr><tr>		<td>2015-2016 1</td>
		<td>B1328320</td>
		<td>B1328320.12</td>
		<td>学术英语读写</td>
<td>C类专门用途类</td>		<td>2</td>
<td style="">	  			83 
</td><td style="">			83
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>I9904120</td>
		<td>I9904120.02</td>
		<td>美术鉴赏</td>
<td>素质教育选修课（艺体类）</td>		<td>2</td>
<td style="">	  			91 
</td><td style="">			91
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>L9800210</td>
		<td>L9800210.01</td>
		<td>军事训练</td>
<td>实践类核心课程</td>		<td>1</td>
<td style="">	  			80 
</td><td style="">			80
</td>		
</tr><tr>		<td>2016-2017 1</td>
		<td>G2225420</td>
		<td>G2225420.01</td>
		<td>大型机DB2</td>
<td>专业核心课程</td>		<td>2</td>
<td style="">	  			73 
</td><td style="">			73
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>B1498910</td>
		<td>B1498910.12</td>
		<td>网球D</td>
<td>大学体育IV</td>		<td>1</td>
<td style="">	  			85 
</td><td style="">			85
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>I1904920</td>
		<td>I1904920.01</td>
		<td>空天信息技术概论</td>
<td>素质教育选修课（自然科学类）</td>		<td>2</td>
<td style="">	  			90 
</td><td style="">			90
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>B9800320</td>
		<td>B9800320.55</td>
		<td>形势与政策</td>
<td>思想政治理论课</td>		<td>2</td>
<td style="">	  			87 
</td><td style="">			87
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>B1600220</td>
		<td>B1600220.13</td>
		<td>中国近现代史纲要</td>
<td>思想政治理论课</td>		<td>2</td>
<td style="">	  			88 
</td><td style="">			88
</td>		
</tr><tr>		<td>2016-2017 1</td>
		<td>I2219620</td>
		<td>I2219620</td>
		<td>“互联网+”创新创业项目从0到1的最佳实践</td>
<td>素质教育选修课程</td>		<td>2</td>
<td style="">	  			90 
</td><td style="">			90
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>B1600130</td>
		<td>B1600130.03</td>
		<td>思想道德修养与法律基础</td>
<td>思想政治理论课</td>		<td>3</td>
<td style="">	  			85 
</td><td style="">			85
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>B9800110</td>
		<td>B9800110.36</td>
		<td>军事理论</td>
<td>军事理论、体育</td>		<td>1</td>
<td style="">	  			88 
</td><td style="">			88
</td>		
</tr><tr>		<td>2016-2017 1</td>
		<td>G2225230</td>
		<td>G2225230.02</td>
		<td>交易中间件技术CICS</td>
<td>专业核心课程</td>		<td>3</td>
<td style="">	  			76 
</td><td style="">			76
</td>		
</tr><tr>		<td>2016-2017 1</td>
		<td>B1600360</td>
		<td>B1600360.07</td>
		<td>毛泽东思想和中国特色社会主义理论体系概论</td>
<td>思想政治理论课</td>		<td>6</td>
<td style="">	  			67 
</td><td style="">			67
</td>		
</tr><tr>		<td>2015-2016 1</td>
		<td>B1427810</td>
		<td>B1427810.06</td>
		<td>综合C</td>
<td>大学体育III</td>		<td>1</td>
<td style="">	  			68 
</td><td style="">			68
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>D0400340</td>
		<td>D0400340.08</td>
		<td>大学物理Ⅰ</td>
<td>学科通识课程</td>		<td>4</td>
<td style="">	  			60 
</td><td style="">			60
</td>		
</tr><tr>		<td>2016-2017 1</td>
		<td>G2231520</td>
		<td>G2231520.01</td>
		<td>信息安全工程</td>
<td>本专业选修课</td>		<td>2</td>
<td style="">	  			62 
</td><td style="">			62
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>E2200440</td>
		<td>E2200440.06</td>
		<td>数据结构与算法</td>
<td>学科基础课程</td>		<td>4</td>
<td style="">	  			81 
</td><td style="">			81
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>F2200210</td>
		<td>F2200210.02</td>
		<td>信息工程导论</td>
<td>学科拓展课程</td>		<td>1</td>
<td style="">	  			87 
</td><td style="">			87
</td>		
</tr><tr>		<td>2015-2016 1</td>
		<td>F2220120</td>
		<td>F2220120.02</td>
		<td>嵌入式系统导论</td>
<td>本专业选修课</td>		<td>2</td>
<td style="">	  			83 
</td><td style="">			83
</td>		
</tr><tr>		<td>2015-2016 1</td>
		<td>E2200740</td>
		<td>E2200740.03</td>
		<td>计算机组成原理与结构</td>
<td>学科基础课程</td>		<td>4</td>
<td style="">	  			63 
</td><td style="">			63
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>B1400210</td>
		<td>B1400210.36</td>
		<td>大学体育II</td>
<td>军事理论、体育</td>		<td>1</td>
<td style="">	  			81 
</td><td style="">			81
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>E2201930</td>
		<td>E2201930.01</td>
		<td>应用数学基础</td>
<td>学科基础课程</td>		<td>3</td>
<td style="">	  			86 
</td><td style="">			86
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>I1906620</td>
		<td>I1906620.01</td>
		<td>MATLAB使用详解</td>
<td>素质教育选修课（自然科学类）</td>		<td>2</td>
<td style="">	  			90 
</td><td style="">			90
</td>		
</tr><tr>		<td>2016-2017 1</td>
		<td>E2201420</td>
		<td>E2201420.03</td>
		<td>系统分析与设计（含UML）</td>
<td>学科基础课程</td>		<td>2</td>
<td style="">	  			86 
</td><td style="">			86
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>B1400110</td>
		<td>B1400110.05</td>
		<td>大学体育I</td>
<td>军事理论、体育</td>		<td>1</td>
<td style="">	  			71 
</td><td style="">			71
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>E2201330</td>
		<td>E2201330.05</td>
		<td>软件工程基础</td>
<td>学科基础课程</td>		<td>3</td>
<td style="">	  			78 
</td><td style="">			78
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>E2200140</td>
		<td>E2200140.02</td>
		<td>C语言程序设计</td>
<td>学科基础课程</td>		<td>4</td>
<td style="">	  			93 
</td><td style="">			93
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>C1600830</td>
		<td>C1600830.02</td>
		<td>哲学通论</td>
<td>交叉通识课程</td>		<td>3</td>
<td style="">	  			78 
</td><td style="">			78
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>J9515220</td>
		<td></td>
		<td>设计、制作小作品</td>
<td>创新与拓展项目</td>		<td>2</td>
<td style="">	  			88 
</td><td style="">			88
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>E2201140</td>
		<td>E2201140.05</td>
		<td>计算机网络基础</td>
<td>学科基础课程</td>		<td>4</td>
<td style="">	  			75 
</td><td style="">			75
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>D1000160</td>
		<td>D1000160.05</td>
		<td>微积分I</td>
<td>学科通识课程</td>		<td>6</td>
<td style="">	  			73 
</td><td style="">			73
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>D1000250</td>
		<td>D1000250.33</td>
		<td>微积分II</td>
<td>学科通识课程</td>		<td>5</td>
<td style="">	  			68 
</td><td style="">			68
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>E2201040</td>
		<td>E2201040.03</td>
		<td>操作系统基础</td>
<td>学科基础课程</td>		<td>4</td>
<td style="">	  			76 
</td><td style="">			76
</td>		
</tr><tr>		<td>2014-2015 1</td>
		<td>B1300140</td>
		<td>B1300140.37</td>
		<td>通用英语</td>
<td>外语</td>		<td>4</td>
<td style="">	  			72 
</td><td style="">			72
</td>		
</tr><tr>		<td>2014-2015 2</td>
		<td>E2201530</td>
		<td>E2201530.04</td>
		<td>数字逻辑设计</td>
<td>本专业选修课</td>		<td>3</td>
<td style="">	  			76 
</td><td style="">			76
</td>		
</tr><tr>		<td>2015-2016 1</td>
		<td>G2225530</td>
		<td>G2225530.01</td>
		<td>UNIX操作系统基础</td>
<td>专业核心课程</td>		<td>3</td>
<td style="">	  			89 
</td><td style="">			89
</td>		
</tr><tr>		<td>2016-2017 1</td>
		<td>K2226620</td>
		<td>K2226620.06</td>
		<td>综合应用设计 II</td>
<td>实践类核心课程</td>		<td>2</td>
<td style="">	  			88 
</td><td style="">			88
</td>		
</tr><tr>		<td>2015-2016 1</td>
		<td>E2200640</td>
		<td>E2200640.01</td>
		<td>面向对象程序设计(java)</td>
<td>学科基础课程</td>		<td>4</td>
<td style="">	  			95 
</td><td style="">			95
</td>		
</tr><tr>		<td>2015-2016 1</td>
		<td>F2201620</td>
		<td>F2201620.04</td>
		<td>IT工程师职业基础</td>
<td>学科拓展课程</td>		<td>2</td>
<td style="">	  			77 
</td><td style="">			77
</td>		
</tr><tr>		<td>2015-2016 2</td>
		<td>G2225130</td>
		<td>G2225130.01</td>
		<td>COBOL程序设计</td>
<td>专业核心课程</td>		<td>3</td>
<td style="">	  			81 
</td><td style="">			81
</td>		
</tr></tbody>
</table>
</div>
<script type="text/javascript">
  var clearCheckbox_grid21344342991 = function() {
    jQuery("#grid21344342991").find(".box:checkbox").removeProp("checked");
    jQuery("#grid21344342991").find(".gridselect-top :checkbox").removeProp("checked");
    return true;
  }
  page_grid21344342991 = bg.page("/eams/teach/grade/course/person!historyCourseGrade.action","");
  {
    var _paramstring = 'projectType=MAJOR';
    var _params = _paramstring.split('&');
    for (var i = 0; i < _params.length; i++) {
      _params[i] = decodeURIComponent(_params[i]);
    }
    _paramstring = _params.join('&');
    page_grid21344342991.target("",'grid21344342991').action("/eams/teach/grade/course/person!historyCourseGrade.action").addParams(_paramstring).orderBy("null");
  }
  bg.ui.grid.init('grid21344342991',page_grid21344342991);
</script>
</body>
</html>
"""