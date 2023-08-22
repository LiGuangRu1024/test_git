# 时间：2023/8/22 15:55
# 人员: 莉光哈哈哈
# 设置机器人提醒
import time

import requests
import jenkins


def get_jenkins_data():
    data = {
        'j_username': 'zhangyr',
        'j_password': 'Luckylhia1024@',
        'from': '/',
        'remember_me': 'on',
        'Submit': ''

    }
    login_url = 'http://124.71.189.186:8130/j_spring_security_check'

    session = requests.Session()

    session.post(url=login_url, data=data, verify=False)

    jenkins_url = 'http://124.71.189.186:8130/job/test_pipeline/api/json?pretty=true'
    res_tmp = session.get(url=jenkins_url).json()
    latest_build_url = res_tmp['builds'][0]['url']

    # build_info_url = latest_build_url + 'allure/widgets/summary.json'
    # allure_report_url = latest_build_url + 'allure'
    # res = session.get(url=build_info_url).json()
    # print(res)
    # return res, allure_report_url


def send_content_by_robot():
    # res, allure_report_url = get_jenkins_data()
    # # api_count_nums = api_count.wall_floder()
    #
    # failed_nums = res['statistic']['failed']
    # broken_nums = res['statistic']['broken']
    # skipped_nums = res['statistic']['skipped']
    # passed_nums = res['statistic']['passed']
    # unknown_nums = res['statistic']['unknown']
    # totle_nums = res['statistic']['total']
    # time_start = res['time']['start'] / 1000
    # time_stop = res['time']['stop'] / 1000
    # build_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_start))
    # build_stop_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stop))
    server = jenkins.Jenkins('http://124.71.189.186:8130', 'zhangyr', 'Luckylhia1024@')
    # print(server.get_all_jobs())
    # build_number = server.get_job_info('test_pipeline')['lastBuild']['number']
    # build_states: str = server.get_build_info('test_pipeline', build_number)['result']
    # if build_states.startswith('FAIL'):
    #     build_states_qcl = 'Failure'
    # elif build_states.startswith('UN'):
    #     build_states_qcl = 'Unstable'
    # elif build_states.startswith('SUC'):
    #     build_states_qcl = 'Success'

    markdown_content = {
        "msgtype": "markdown",
        "markdown": {
            "content": "# <font color='info'>test_pipiline接口自动化测试</font> \n"
                       "## <font color='info'>已构建完成</font> \n"
                       "\n"
                       "\n"
                       # f">### <font color='info'>构建状态: {build_states_qcl}</font>\n"
                       # f">### <font color='info'>TotalCase: {totle_nums}</font> \n"
                       # f">### <font color='info'>Passed: {passed_nums}</font> \n"
                       # f">### <font color='warning'>Failed: {failed_nums}</font> \n"
                       # f">### <font color='info'>Skipped: {skipped_nums}</font> \n"
                       # f">### <font color='warning'>Broken: {broken_nums}</font> \n"
                       # f">### <font color='warning'>Unknown: {unknown_nums}</font> \n"
                       # f">### <font color='comment'>构建开始时间: {build_start_time}</font> \n"
                       # f">### <font color='comment'>构建结束时间: {build_stop_time}</font>\n"
                       # f">### 具体见 Allure 报告: [{allure_report_url}]({allure_report_url})\n"
                       "\n"
                       "\n"
                       "\n"
        }
    }
    requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=986eceaa-d0b2-4a00-aeca-f0ef196e1d8e',
                  json=markdown_content, verify=False)


send_content_by_robot()