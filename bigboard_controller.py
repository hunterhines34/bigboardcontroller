# Imports
import PySimpleGUI as sg
import subprocess, time, ping3

# Reboot bigboard(s)
def reboot_board(pc):
    subprocess.call(f'shutdown /r /m {pc} /t 0')           

# Ping bigboard - first round
def ping_board_first(pc):
    try:
        response = ping3.ping(pc, unit='ms')

        if response > 0:
            first_ping_status = 'active'
        else:
            first_ping_status = 'inactive'
        return first_ping_status     
    except ValueError as error:
        return f'An error occurred during the operation: {error}'  

# Main entry point
def main():
    # ER bigboards layout
    er_layout = [
                    [sg.Checkbox('D20073006', key='D20073006'), sg.Text('-- DRH ER Bigboard')], [sg.Checkbox('D21053183', key='D21053183'), sg.Text('-- JCH ER Bigboard')]
                ]
    # ER bigboards layout
    tower_layout = [
                        [sg.Checkbox('D21053184', key='D21053184'), sg.Text('-- DRH T2 Bigboard')], [sg.Checkbox('D21053185', key='D21053185'), sg.Text('-- DRH T3 Bigboard')]
                   ]                  
    # Lab bigboards layout
    lab_layout = [
                    [sg.Checkbox('DVLABTV1', key='DVLABTV1'), sg.Text('-- DRH LAB TV1 Bigboard')], [sg.Checkbox('DVLABTV2', key='DVLABTV2'), sg.Text('-- DRH LAB TV2 Bigboard')],
                    [sg.Checkbox('DVLABTV3', key='DVLABTV3'), sg.Text('-- DRH LAB TV3 Bigboard')], [sg.Checkbox('DVLABTV4', key='DVLABTV4'), sg.Text('-- DRH LAB TV4 Bigboard')],
                 ]
    # ACU bigboards layout
    acu_layout = [
                    [sg.Checkbox('DVACUTV', key='DVACUTV'), sg.Text('-- DRH ACU Bigboard')], [sg.Checkbox('D21093220', key='D21093220'), sg.Text('-- TEST COMP')]
                 ]
    # IT bigboards layout
    it_layout = [
                    [sg.Checkbox('ITBigBoard', key='ITBigBoard'), sg.Text('-- DRH IT IN/OUT Bigboard')]
                ]             
    # Cafe bigboards layout
    cafe_layout = [
                    [sg.Checkbox('DVCAFETV10', key='DVCAFETV10'), sg.Text('-- DRH CAFE Front Bigboard')], [sg.Checkbox('DVCAFE2TV10', key='DVCAFE2TV10'), sg.Text('-- DRH CAFE Back Bigboard')],
                  ]
    # Tab / Tab group layout
    tab_layout = [
                    [sg.TabGroup([[sg.Tab('ER Bigboards', er_layout, title_color=None, border_width=10),
                     sg.Tab('Tower Bigboards', tower_layout, title_color=None, border_width=10),
                     sg.Tab('Lab Bigboards', lab_layout, title_color=None, border_width=10),
                     sg.Tab('ACU Bigboards', acu_layout, title_color=None, border_width=10),
                     sg.Tab('IT Bigboards', it_layout, title_color=None, border_width=10),
                     sg.Tab('Cafe Bigboards', cafe_layout, title_color=None, border_width=10)]])],
                    [sg.Multiline(size=(80,10), autoscroll=True, reroute_stdout=True, key='OUTPUT')],
                    [sg.Button('Reboot Bigboard(s)', key='REBOOT', size=(72, 0))]
                 ]  
    # Create window structure
    window = sg.Window('Bigboard Control Center', tab_layout)
    # Keep window alive until user closes
    while True:
        event, values = window.read()

        # If window closed, kill application
        if event == sg.WIN_CLOSED:
            break
        # If event is D20073006
        if event == 'REBOOT' and values['D20073006']:
            computer = 'D20073006'
            reboot_board(computer)
            window['OUTPUT'].print(f'Rebooting {computer}...')
            window['OUTPUT'].print(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')
        # If event is D21053183
        if event == 'REBOOT' and values['D21053183']:
            computer = 'D21053183'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')    
        # If event is D21053184
        if event == 'REBOOT' and values['D21053184']:
            computer = 'D21053184'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')
        # If event is D21053185
        if event == 'REBOOT' and values['D21053185']:
            computer = 'D21053185'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')
        # If event is DVLABTV1
        if event == 'REBOOT' and values['DVLABTV1']:
            computer = 'DVLABTV1'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')
        # If event is DVLABTV2
        if event == 'REBOOT' and values['DVLABTV2']:
            computer = 'DVLABTV2'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')            
        # If event is DVLABTV3
        if event == 'REBOOT' and values['DVLABTV3']:
            computer = 'DVLABTV3'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')
        # If event is DVLABTV4
        if event == 'REBOOT' and values['DVLABTV4']:
            computer = 'DVLABTV4'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')
        # If event is DVACUTV
        if event == 'REBOOT' and values['DVACUTV']:
            computer = 'DVACUTV'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')
        # If event is ITBigBoard
        if event == 'REBOOT' and values['ITBigBoard']:
            computer = 'ITBigBoard'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')
        # If event is DVCAFETV10
        if event == 'REBOOT' and values['DVCAFETV10']:
            computer = 'DVCAFETV10'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...') 
        # If event is DVCAFE2TV10
        if event == 'REBOOT' and values['DVCAFE2TV10']:
            computer = 'DVCAFE2TV10'
            reboot_board(computer)
            window['OUTPUT'].update(f'Rebooting {computer}...')
            window['OUTPUT'].update(f'{computer} has been rebooted successfully.')
        else:
            window['OUTPUT'].update('Please choose a computer to reboot...')
        # If event is D21093220 -- TEST COMP
        if event == 'REBOOT' and values['D21093220']:
            computer = 'D21093220'
            
            first_ping = ping_board_first(computer)

            if first_ping == "active":
                reboot_board(computer)
                window['OUTPUT'].update(f'Rebooting {computer}...', text_color='red')
                window['OUTPUT'].print('\n')
                
                for i in range(50):
                    window['OUTPUT'].print(f'pending reboot status...', text_color='orange')
                window['OUTPUT'].print(f'\n{computer} has been rebooted successfully.', text_color='green')
            else:
                window['OUTPUT'].update(f'{computer} appears to be offline...', text_color='red')                               

    # Kill window after event == 'WIN_CLOSED'
    window.close()                   

# Set environment vars
if __name__ == '__main__':
    main()