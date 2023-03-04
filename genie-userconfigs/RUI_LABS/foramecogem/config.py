def clean_text(file, text: str):
    "remove text and the line from specified file"
    with open(file,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if text not in line:
                f.write(line)
        f.truncate()


def write_data(file, data: dict):
    from configparser import ConfigParser
    config = ConfigParser()
    config.add_section('ecogem')
    data_in_list = [(k,v) for k,v in data.items()]
    for i in data_in_list:
        config.set('ecogem', i[0], i[1])

    with open(file, 'a') as f:
            config.write(f)


def select_files(path):
    from pathlib import Path
    path = Path(path)
    
    files = sorted(path.glob('*'))
    # exclude readme files
    filtered_paths = [f for f in files if 'readme' not in f.stem]
    # exclude python files
    filtered_paths = [f for f in filtered_paths if 'py' not in f.suffix]

    return filtered_paths


def main(path, data: dict):
    config_files = select_files(path)

    # convert data into list
    data_in_list = [(k,v) for k,v in data.items()]

    for file in config_files:
        # clean text stored in keys
        for i in data_in_list:
            clean_text(file, i[0])
        # write configuration
        write_data(file, data)

if __name__ == '__main__':
    config = {
        'eg_par_ecogem_plankton_file': "'8P7Z4F.eco'",
        'eg_par_ecogem_grazing_file': "'FORAMECOGEM.zoo'",
        'eg_ah_size_ratio': '0.002',
        'eg_ss_tradeoff_a': '0.68',
        'eg_ss_tradeoff_h': '0.1',
        'eg_sn_tradeoff_a': '0.45',
        'eg_sn_tradeoff_h': '0.45'
    }
    
    config2 = {
        'eg_par_ecogem_plankton_file': "'8P7Z4F.eco'",
        'eg_par_ecogem_grazing_file': "'FORAMECOGEM.zoo'", #use reduced growth rate
        'eg_ah_size_ratio': '0.002',
        'eg_ss_tradeoff_a': '0.35',
        'eg_ss_tradeoff_h': '0.1',
        'eg_sn_tradeoff_a': '0.3',
        'eg_sn_tradeoff_h': '0.5'
    }
    main('/Users/yingrui/cgenie.muffin.rui/genie-userconfigs/RUI_LABS/foramecogem', data=config)

