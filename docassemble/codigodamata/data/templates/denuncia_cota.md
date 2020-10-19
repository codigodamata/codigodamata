${tipo_procedimento} Código: **${simp}**

REQUERIDO:
% for  requerido in requeridos:
**${requerido.name.full()}**,
% endfor

&nbsp;

&nbsp;

&nbsp;

&nbsp;

${indentation} Meritíssimo Juiz,


&nbsp;

&nbsp;

&nbsp;

&nbsp;

${indentation} O **${parte_autora}**, por seu promotor de Justiça signatário, oferece denúncia contra 
% for  requerido in requeridos:
**${requerido.name.full()}**
% endfor, 
nos termos da denúncia anexa, ocasião em que se requer:

&nbsp;

&nbsp;

1. a juntada aos autos de certidão criminal de 
% for  requerido in requeridos:
**${requerido.name.full()}**,
% endfor
expedidas pelo cartório judicial desta Comarca e, ainda, dos cartórios judiciais em que conste registro de antecedentes criminais apontados pelo sistema SIAP do E. Tribunal de Justiça do Estado de Mato Grosso, inclusive com informações acerca do trâmite de inquéritos policiais em andamento, bem como eventual certidão de trânsito em julgado;
2. seja oficiado ao Instituto Nacional de Identificação Criminal e ao Instituto de Identificação Criminal do Estado de Mato Grosso requisitando certidões de antecedentes criminais em nome do denunciado;
3. que, após o recebimento da denúncia, seja comunicado ao Distribuidor, ao Instituto de Identificação, bem como alimentado o banco de dados do Sistema Nacional de Informação Criminal (SINIC), conforme PROVIMENTO Nº. 41/2011 – CGJ;

% if pedido_reparacao_dano:

&nbsp;

**DA REPARAÇÃO DO DANO AMBIENTAL**

${indentation} O art. 20 da Lei 9.605/98 (Lei dos Crimes Ambientais) dispõe que:

&nbsp;

> "Art. 20. A sentença penal condenatória, sempre que possível, fixará o valor mínimo para reparação dos danos causados pela infração, considerando os prejuízos sofridos pelo ofendido ou pelo meio ambiente."

&nbsp;

${indentation} Com base neste preceito legal, o *Parquet* requer fixação de valor mínimo à reparação do dano ambiental em questão nos seguintes termos:

> ${indentation} ${pedido_reparacao_dano}

% endif

% if pedir_medida_cautelar_diversa_prisao:

&nbsp;

**DA MEDIDA CAUTELAR DIVERSA DA PRISÃO**

&nbsp;

${indentation} ${medida_cautelar_desmatamento}
% endif

% if cabimento_suspro: 

&nbsp;

&nbsp;

**DA PROPOSTA DE COMPOSIÇÃO CIVIL DO DANO AMBIENTAL MATERIAL E EXTRAPATRIMONIAL**

&nbsp;

${indentation} ${proposta_composicao_dano_material_desmate}
${indentation} ${proposta_composicao_dano_extra}

&nbsp;
&nbsp;

**DA SUSPENSÃO CONDICIONAL DO PROCESSO**

&nbsp;

&nbsp;

${indentation} ${proposta_suspro}
% else:

&nbsp;
&nbsp;

${indentation} ${justificativa_nao_cabimento_suspro}
% endif

&nbsp;
&nbsp;

${indentation} ${cidade}, ${data_hoje}

&nbsp;
&nbsp;
&nbsp;

${indentation} **${subscritor}**

${indentation} ${cargo_subscritor}
