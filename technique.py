def get_tech(tech_name):
    send_list = []
    if tech_name == 'YUSAMADive':
        send_list.append('https://clips.twitch.tv/ShyTemperedGiraffeDerp')
        send_list.append('https://www.youtube.com/watch?v=fyCtDxg9ohM')
        send_list.append('https://www.youtube.com/watch?v=5mjjQt7-dLI')
    elif tech_name == 'CrouchGrabs':
        send_list.append('https://www.youtube.com/watch?v=hKZkzWJI_Mo')
    elif tech_name == 'Fast9' or tech_name == 'DiveSkip':
        send_list.append('https://www.youtube.com/watch?v=k42Pi0S2xzg')
    elif tech_name == 'ForbiddenPipeJump' or tech_name == 'FPJ':
        send_list.append('https://www.youtube.com/watch?v=EyYMkDNFagI')
    elif tech_name == 'PipeJump' or tech_name == 'PJ':
        send_list.append('https://www.youtube.com/watch?v=jDzDq6_CpCA')
    elif tech_name == '13CornerJump':
        send_list.append('https://www.youtube.com/watch?v=MOMRmRA7Ykg')
    elif tech_name == 'SpiralSkip':
        send_list.append('https://www.youtube.com/watch?v=WZUohS0QNCI')
    elif tech_name == 'Hdnoftr':
        send_list.append('https://www.youtube.com/watch?v=keKOAGSsFJg')
    else:
        send_list.append(f'{tech_name} is not technique name')
    return send_list