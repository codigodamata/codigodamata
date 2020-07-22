[STOP_INDENTATION]

EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA UNIDADE JUDICIAL **${UNIDADE_JUDICIAL}** DA COMARCA DE **${COMARCA}**

&nbsp;
&nbsp;
&nbsp;
&nbsp;

${TIPO_PROCEDIMENTO} Código: **${NUM_PROCESSO}**

REQUERIDO: **${REQUERIDOS}**

&nbsp;
&nbsp;
&nbsp;
&nbsp;


[START_INDENTATION] 

O **${PARTE_AUTORA}**, com fundamento nas normas constitucionais e legais vigentes e nos elementos colhidos no  procedimento investigatório em epígrafe, vem à presença de Vossa Excelência oferecer

[STOP_INDENTATION]

[BOLDCENTER] DENÚNCIA

em desfavor de

> **${REQUERIDOS}**, ${QUALIFICACAO_REQUERIDO}

pela prática, em tese, dos seguintes fatos delituosos:

[START_INDENTATION]
Segundo apurado no ${TIPO_PROCEDIMENTO} N.**${NUM_PROCESSO}** em **${DATA_FATO}**, **${HORA_FATO}** no local **${LOCAL_FATO}**, nas proximidades das coordenadas **${COORDENADAS}**, o requerido **${REQUERIDOS}** **${PRECEITO_PRIMARIO}** em uma área total de **${AREA_DESTRUIDA}** hectares de ${TIPO_VEGETACAO}, conforme constatado no ${DOC_PROVA_MATERIALIDADE}, elaborado pelo órgão de fiscalização ambiental competente, a saber, ${ORGAO_DOC_PROVA_MATERIALIDADE}.

${NOTICIA_CRIME}

${DILIGENCIA_REALIZADA}

${PARAGRAFO_MATERIALIDADE}

${REPRESENTACAO}.

Ante o exposto, o **${PARTE_AUTORA}**, por seu promotor de Justiça signatário, **DENUNCIA ${REQUERIDOS}**, como incurso nas sanções previstas no **${FUNDAMENTO_NORMATIVO}** requerendo que, recebida e autuada esta inicial, seja ele citado para responder à acusação, e, após a formação da culpa, com observância do contraditório e da ampla defesa, seja prolatada sentença penal condenatória.

${CIDADE}, ${DATA_HOJE}

[STOP_INDENTATION]

&nbsp;
&nbsp;

[BOLDCENTER] ${SUBSCRITOR}

[BOLDCENTER] ${CARGO_SUBSCRITOR}

&nbsp;
&nbsp;
&nbsp;
&nbsp;

**ROL DE TESTEMUNHAS**

**${TESTEMUNHAS}**

[PAGEBREAK] 

${TIPO_PROCEDIMENTO} Código: **${NUM_PROCESSO}**

REQUERIDO: **${REQUERIDOS}**

[START_INDENTATION]

&nbsp;
&nbsp;

Meritíssimo Juiz,

&nbsp;
&nbsp;

O **${PARTE_AUTORA}**, por seu promotor de Justiça signatário, oferece denúncia contra **${REQUERIDOS}**, nos termos da denúncia anexa, ocasião em que se requer:

a juntada aos autos de certidão criminal de **${requeridos}** expedidas pelo cartório judicial desta Comarca e, ainda, dos cartórios judiciais em que conste registro de antecedentes criminais apontados pelo sistema SIAP do E. Tribunal de Justiça do Estado de Mato Grosso, inclusive com informações acerca do trâmite de inquéritos policiais em andamento, bem como eventual certidão de trânsito em julgado;

seja oficiado ao Instituto Nacional de Identificação Criminal e ao Instituto de Identificação Criminal do Estado de Mato Grosso requisitando certidões de antecedentes criminais em nome do denunciado;

que, após o recebimento da denúncia, seja comunicado ao Distribuidor, ao Instituto de Identificação, bem como alimentado o banco de dados do Sistema Nacional de Informação Criminal (SINIC), conforme PROVIMENTO Nº. 41/2011 – CGJ;
${PEDIDO_REPARACAO_DANO}
% if pedir_medida_cautelar_diversa_prisao:
${MEDIDA_CAUTELAR_DESMATAMENTO}
% endif
% if cabimento_suspro: 
# PROPOSTA DE COMPOSIÇÃO CIVIL DO DANO AMBIENTAL MATERIAL E EXTRAPATRIMONIAL
${proposta_composicao_dano_material_desmate}
${proposta_composicao_dano_extra}
# DA SUSPENSÃO CONDICIONAL DO PROCESSO
${PROPOSTA_SUSPRO}
% else:
${justificativa_nao_cabimento_suspro}
% endif

${CIDADE}, ${DATA_HOJE}

[STOP_INDENTATION]

&nbsp;
&nbsp;
&nbsp;

[BOLDCENTER] ${SUBSCRITOR}

[BOLDCENTER] ${CARGO_SUBSCRITOR}
