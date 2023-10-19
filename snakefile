import my_utils
import plot_his

COUNTRY=['Afghanistan', 'Serbia', 'Croatia']

rule all:
  input:
    expand('{country}.png', country=COUNTRY)
   
rule download_data:
  output:
    'Agrofood_co2_emission.csv'
  shell:
    'wget -O {output} "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr"'
                                         
rule get_data:
  input:
    'Agrofood_co2_emission.csv'
  output:
    '{x}_Fires.txt'
  shell:
    'python3 my_utils.py {input} "{wildcards.x}" "{output}"'

rule plot_data:
  input:
    '{w}_Fires.txt'
  output:
    '{w}.png'
  shell:
    'python3 plot_his.py "{input}" "{output}" "{wildcards.w}" Fires Freq.'
