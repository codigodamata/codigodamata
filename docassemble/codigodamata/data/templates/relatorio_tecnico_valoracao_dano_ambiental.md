[STOP_INDENTATION]


[BOLDCENTER] RELATÓRIO TÉCNICO

&nbsp;
&nbsp;

PROC. N. ${SIMP}

REQUERIDO: ${REQUERIDOS}


&nbsp;
&nbsp;


[START_INDENTATION] 

# INTRODUÇÃO

A presente valoração do dano ambiental baseia-se nos trabalhos de Roquette (2019) e Gonzaga e Roquette (2020).

A utilização da precificação (circunstanciada) de emissões de carbono como critério objetivo para a valoração do dano ambiental é uma proposta inicial de estudo, baseada em precedentes do STJ de fixação dos danos extrapatrimoniais, principalmente o [**AgRESP 1323104/GO**](https://consciencia.eco.br/index.php?title=AgRESP_1323104/GO) em que se fundamentou que *“...não é necessário ser um cientista e especialista no tema para afirmar que a queimada da cana-de-açúcar causa poluição atmosférica e contribui para o famigerado efeito estufa e aquecimento global...”. Além disso, outros precedentes fazem expressa menção à questão climática, tais como RESP 1.000.731/RO e RESP 650.728/SC*.

Para a precificação das emissões de carbono, utilizou-se o método descrito em [Jacoski et al. (2014)](https://periodicos.pucpr.br/index.php/estudosdebiologia/article/view/22972). 

A valoração do dano material foi inspirada na proposta de [Roquette (2019)](http://ucs.br/etc/revistas/index.php/direitoambiental/article/view/7981).

Utilizaram-se os seguintes critérios:

- dano material: ${texto_metodo_reparacao_escolhido}
- dano extrapatrimonial: ${nome_metodo_extrapatrimonial}
- informações complementares:  ${info_utilizadas}
  
# CARACTERÍSTICAS  
  
As características do desflorestamento ilegal são as seguintes

## Características comuns:

-  **Área total desmatada igual a  ${area_desmate_total}** hectares;
-  ${BIOMA};
-  ${remocao_solo};
-  ${potencial_resiliencia};
-  ${ocorrencia_queimadas};
-  ${presenca_gado};
-  Dano em APP, ARL e AU:  ${area_desmate_insuscet_recup}
-  Dano em APP, ARL e AU irrecuperável: ${area_desmate_insuscet_irrecup}
-  Dano em área prístina passível de desmatamento (porém realizado de forma ilegal):  ${area_desmate_suscet_veg_prim}
-  Dano em área de vegetação secundária em área consolidada passível de desmatamento (porém realizado de forma ilegal): ${area_desmate_suscet_veg_sec}
-  Circunstâncias desfavoráveis: ${circunstancias_dano}.

&nbsp;
&nbsp;
&nbsp;

# CONCLUSÃO

## Danos materiais
% if area_desmate_insuscet_recup:
### Desmatamento em APP, ARL e AU: 
Intervenções necessárias: ${intervencoes_cabiveis_insuscet_recup}.
% endif

% if area_desmate_insuscet_irrecup:
### Desmatamento em APP, ARL e AU irrecuperável: 
Intervenções necessárias: ${intervencoes_cabiveis_desmate_insuscet_irrecup}
% endif

% if area_desmate_suscet_veg_prim:
### Desmatamento em área passível de desmatamento (porém realizado de forma ilegal):
Intervenções necessárias: ${intervencoes_cabiveis_desmate_fora_APP_ARL}
% endif

% if area_desmate_suscet_veg_sec:
### Desmatamento em área consolidada e de vegetação em estágio inicial de regeneração, passível de desmatamento (porém realizado de forma ilegal):
Intervenções necessárias: ${intervencoes_cabiveis_desmate_area_consolidada}
% endif

## Dano extrapatrimonial
Valor do dano extrapatrimonial: **R$ ${dano_extra_patr}**

## Total (danos materiais e extrapatrimoniais)
O valor total dos danos materiais e extrapatrimoniais em pecúnia é de **R$ ${pecunia_total}** .

## Conversão da pecúnia em pagamento "in natura"

Oferece-se como alternativa ao pagamento "in pecunia" conversão de **${percent_conversao_serv_amb*100} %** do valor "in pecunia" mediante a instituição de servidão ambiental perpétua (art. 9º-A da Lei 6.938/81).

${conversao_servidao_ambiental}

São Benefícios da servidão ambiental:

- "A servidão ambiental perpétua equivale, para fins creditícios, tributários e de acesso aos recursos de fundos públicos, à Reserva Particular do Patrimônio Natural - RPPN3, definida no art. 21 da Lei no 9.985, de 18 de julho de 2000" (Art. 9º-B, § 2º, da Lei 6.938/81);

- Poderá comercializar Cota de Reserva Ambiental - CRA, título nominativo representativo de área com vegetação nativa, existente ou em processo de recuperação (art. 44, I, da Lei 12.651/12), após o prazo estipulado.

- Valor lucros cessantes: é compensado pelo caráter perpétuo da servidão ambiental.

- Valor dano extrapatrimonial: é descontado em  **${percent_desc_dano_extra*100} %**
em razão da destinação de uma área suscetível de desmatamento à conservação permanente;

${CIDADE}, ${DATA_HOJE}.

[STOP_INDENTATION]

&nbsp;
&nbsp;

[BOLDCENTER] ${SUBSCRITOR}

[BOLDCENTER] ${CARGO_SUBSCRITOR}