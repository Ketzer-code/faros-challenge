# Exercicio 2

# importing libraries
library(tidyverse)
library(vroom)

# setting working directory
wd <- getwd()

# reading dataframe and renaming columns
shares_df <- vroom(paste0(wd, "/tabela_acoes.csv")) %>%
                dplyr::rename(
                    ticker = `Ação`,
                    client = Cliente,
                    qtd = QTD,
                    price = `PREÇO`
                )

# calculating total invested amount per client
total_invested_per_client <- shares_df %>%
                                mutate(invested_amount = price * qtd) %>%
                                group_by(client) %>%
                                summarise(total_invested_amount = sum(invested_amount))
