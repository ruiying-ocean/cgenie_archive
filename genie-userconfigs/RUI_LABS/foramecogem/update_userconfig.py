import os

def update_foramecogem(directory):
    """A quicker way to update all foramecogem related text configuration.
    This function identifies scripts starting with muffin as targets
    """
    
    
    parameters = {
        'eg_par_ecogem_plankton_file': "'8P7Z4F.eco'",
        'eg_par_ecogem_grazing_file': "'FORAMECOGEM.zoo'",
        'eg_ah_size_ratio': '0.0015',
        'eg_ss_tradeoff_a': '1.0',
        'eg_ss_tradeoff_h': '0.5',
        'eg_sn_tradeoff_a': '0.8',
        'eg_sn_tradeoff_h': '0.5',
        'eg_ctrl_ncrst' : '.false.',
        'eg_ctrl_continuing' : '.false.',
        'eg_ctrl_grazing_explicit': '.true.',
        'eg_ctrl_debug_init': '0',
        'eg_ctrl_debug_eco_init': '.false.',
        'eg_gkernel_cap': '.false.'
    }
    

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.startswith("muffin"):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            updated_lines = []
            for line in lines:
                for key, value in parameters.items():
                    if key in line:
                        line = f"{key}={value}\n"
                updated_lines.append(line)

            with open(file_path, 'w') as file:
                file.writelines(updated_lines)

# Check if the script is being run as a standalone program
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        text_directory = sys.argv[1]
        update_foramecogem(text_directory)
    else:
        print("Please provide the text directory as a command-line argument.")
