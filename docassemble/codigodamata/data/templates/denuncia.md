EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA UNIDADE JUDICIAL **${unidade_judicial}** DA COMARCA DE **${comarca}**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<<<<<<< HEAD
${tipo_procedimento} N. **${simp}**

REQUERIDO:
% for  requerido in requeridos:
**${requerido.name.full()}**,
=======
${tipo_procedimento} N. **${num_processo}**

REQUERIDO:
% for  requerido in requeridos:
**${requerido.name}**,
>>>>>>> 8807a61946a825d83966413b476718e02d56d245
% endfor

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<<<<<<< HEAD
${indentation} O **${parte_autora}**, com fundamento nas normas constitucionais e legais vigentes e nos elementos colhidos no  procedimento investigatório em epígrafe, vem à presença de Vossa Excelência oferecer **DENÚNCIA** em desfavor de
=======
O **${parte_autora}**, com fundamento nas normas constitucionais e legais vigentes e nos elementos colhidos no  procedimento investigatório em epígrafe, vem à presença de Vossa Excelência oferecer **DENÚNCIA** em desfavor de
>>>>>>> 8807a61946a825d83966413b476718e02d56d245

&nbsp;

&nbsp;

% for  requerido in requeridos:
<<<<<<< HEAD
> **${requerido.name.full()}**, ${requerido.qualificacao}
  ${"\n"}
=======
> **${requerido.name}**, ${requerido.qualificacao}

>>>>>>> 8807a61946a825d83966413b476718e02d56d245
% endfor

&nbsp;

&nbsp;

pela prática, em tese, dos seguintes fatos delituosos:

&nbsp;
&nbsp;

<<<<<<< HEAD
% for  fato in fatos:
**DA INFRAÇÃO PENAL PREVISTA NO ${fato.fundamento_normativo.upper()}**

${indentation} ${fato.descricao_fato_tipico_1a_parte} o requerido **${todos_requeridos}** ${fato.descricao_fato_tipico_2a_parte};
=======
Segundo apurado no ${tipo_procedimento} N.**${num_processo}** em **${data_fato}**, **${hora_fato}** no local **${local_fato}**, nas proximidades das coordenadas **${coordenadas}**, o requerido **${requerido.name}** **${preceito_primario}** em uma área total de **${area_destruida}** hectares de ${tipo_vegetacao}, conforme constatado no ${doc_prova_materialidade} N. ${num_doc_prova_materialidade}, da ${orgao_doc_prova_materialidade}.
>>>>>>> 8807a61946a825d83966413b476718e02d56d245

&nbsp;
&nbsp;

<<<<<<< HEAD
${indentation} ${fato.noticia_crime}
=======
${noticia_crime}
>>>>>>> 8807a61946a825d83966413b476718e02d56d245

&nbsp;
&nbsp;

<<<<<<< HEAD
${indentation} ${fato.diligencia_realizada}
=======
${diligencia_realizada}
>>>>>>> 8807a61946a825d83966413b476718e02d56d245

&nbsp;
&nbsp;

<<<<<<< HEAD
${indentation} ${fato.paragrafo_materialidade}
=======
${paragrafo_materialidade}
>>>>>>> 8807a61946a825d83966413b476718e02d56d245

&nbsp;
&nbsp;

<<<<<<< HEAD
${indentation} ${fato.representacao}.
=======
${representacao}.
>>>>>>> 8807a61946a825d83966413b476718e02d56d245

&nbsp;
&nbsp;

<<<<<<< HEAD
% endfor



${indentation} Ante o exposto, o **${parte_autora}**, por seu promotor de Justiça signatário, **DENUNCIA** 
% for  requerido in requeridos:
  **${" " + requerido.name.full()}**,
% endfor
como incurso nas sanções previstas no
% for  fato in fatos:
  **${" " + fato.fundamento_normativo}**,
% endfor
requerendo que, recebida e autuada esta inicial, seja ele citado para responder à acusação, e, após a formação da culpa, com observância do contraditório e da ampla defesa, seja prolatada sentença penal condenatória.

&nbsp;
&nbsp;

${indentation} ${cidade}, ${data_hoje}.


&nbsp;
&nbsp;

${indentation} **${subscritor}**

${indentation} ${cargo_subscritor}

&nbsp;

=======
Ante o exposto, o **${parte_autora}**, por seu promotor de Justiça signatário, **DENUNCIA**  
% for  requerido in requeridos:
  **${requerido.name}**,
% endfor
como incurso nas sanções previstas no **${fundamento_normativo}** requerendo que, recebida e autuada esta inicial, seja ele citado para responder à acusação, e, após a formação da culpa, com observância do contraditório e da ampla defesa, seja prolatada sentença penal condenatória.

&nbsp;
&nbsp;

${cidade}, ${data_hoje}.


&nbsp;
&nbsp;

**${subscritor}**

${cargo_subscritor}

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**ROL DE TESTEMUNHAS**

${testemunhas}


&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

${tipo_procedimento} Código: **${num_processo}**

REQUERIDO: **${requeridos}**


&nbsp;

&nbsp;

&nbsp;

&nbsp;

Meritíssimo Juiz,


&nbsp;

&nbsp;

&nbsp;

&nbsp;

O **${parte_autora}**, por seu promotor de Justiça signatário, oferece denúncia contra 
% for  requerido in requeridos:
**${requerido.name}**
% endfor, 
nos termos da denúncia anexa, ocasião em que se requer:

&nbsp;

&nbsp;

1. a juntada aos autos de certidão criminal de 
% for  requerido in requeridos:
**${requerido.name}**,
% endfor
expedidas pelo cartório judicial desta Comarca e, ainda, dos cartórios judiciais em que conste registro de antecedentes criminais apontados pelo sistema SIAP do E. Tribunal de Justiça do Estado de Mato Grosso, inclusive com informações acerca do trâmite de inquéritos policiais em andamento, bem como eventual certidão de trânsito em julgado;
2. seja oficiado ao Instituto Nacional de Identificação Criminal e ao Instituto de Identificação Criminal do Estado de Mato Grosso requisitando certidões de antecedentes criminais em nome do denunciado;
3. que, após o recebimento da denúncia, seja comunicado ao Distribuidor, ao Instituto de Identificação, bem como alimentado o banco de dados do Sistema Nacional de Informação Criminal (SINIC), conforme PROVIMENTO Nº. 41/2011 – CGJ;
4. ${pedido_reparacao_dano}

% if pedir_medida_cautelar_diversa_prisao:

&nbsp;

**DA MEDIDA CAUTELAR DIVERSA DA PRISÃO**

&nbsp;

${medida_cautelar_desmatamento}
% endif

% if cabimento_suspro: 

&nbsp;

&nbsp;

**DA PROPOSTA DE COMPOSIÇÃO CIVIL DO DANO AMBIENTAL MATERIAL E EXTRAPATRIMONIAL**

&nbsp;

${proposta_composicao_dano_material_desmate}
${proposta_composicao_dano_extra}

&nbsp;
&nbsp;

**DA SUSPENSÃO CONDICIONAL DO PROCESSO**

>>>>>>> 8807a61946a825d83966413b476718e02d56d245
&nbsp;

&nbsp;

<<<<<<< HEAD
&nbsp;

**ROL DE TESTEMUNHAS**

${testemunhas}
=======
${proposta_suspro}
% else:

&nbsp;
&nbsp;

${justificativa_nao_cabimento_suspro}
% endif

${cidade}, ${data_hoje}

&nbsp;
&nbsp;
&nbsp;

**${subscritor}**
${cargo_subscritor}
>>>>>>> 8807a61946a825d83966413b476718e02d56d245
