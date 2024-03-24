# Introdução:
Este README descreve a função de recompensa implementada para o AWS DeepRacer, um veículo autônomo de corrida desenvolvido pela Amazon Web Services (AWS). A função de recompensa desempenha um papel crucial no treinamento do modelo de aprendizado de máquina do DeepRacer, pois define como o veículo é recompensado ou penalizado com base em seu desempenho durante a corrida.

## Função de Recompensa:
A função de recompensa é implementada na linguagem de programação Python e recebe um conjunto de parâmetros que descrevem o estado atual do veículo e do ambiente. Vamos analisar cada componente da função de recompensa e sua respectiva razão de existência:

### all_wheels_on_track:
Esta variável booleana indica se todas as rodas do veículo estão dentro dos limites da pista.
Razão de uso: Penalizar o veículo caso saia da pista, incentivando-o a permanecer na área designada para a corrida.

### distance_from_center:
Representa a distância perpendicular do veículo ao centro da pista.
Razão de uso: Oferecer recompensas com base na proximidade do veículo ao centro da pista, incentivando-o a permanecer na trajetória ideal.

### progress:
Indica o progresso do veículo ao longo da pista, representado como uma porcentagem.
Razão de uso: Fornecer uma recompensa adicional quando o veículo está próximo da linha de chegada, incentivando-o a completar a corrida.

### speed:
Representa a velocidade atual do veículo.
Razão de uso: Oferecer recompensas ou penalidades com base na velocidade do veículo para incentivar um comportamento de condução suave e eficiente.

### steps:
Indica o número de passos (ou etapas de tempo) decorridos na simulação.
Razão de uso: Estabelecer um limite de tempo para a corrida e penalizar o veículo caso esse limite seja excedido.

### track_width:
Define a largura da pista.
Razão de uso: Utilizado para calcular os marcadores de distância do veículo ao centro da pista.
Utilização da Função de Recompensa:
Para utilizar a função de recompensa no treinamento do modelo do AWS DeepRacer, você pode seguir estes passos:

## Considerações Finais:
A função de recompensa desempenha um papel fundamental no treinamento do modelo do AWS DeepRacer, influenciando diretamente o comportamento do veículo durante a corrida. Ao entender e ajustar adequadamente os componentes da função de recompensa, você pode melhorar significativamente o desempenho e a eficácia do modelo, permitindo que o DeepRacer navegue com sucesso pela pista.