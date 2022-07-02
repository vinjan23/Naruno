#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import time

from accounts.get_balance import GetBalance
from accounts.get_sequance_number import GetSequanceNumber
from lib.log import get_logger

logger = get_logger("TRANSACTIONS")


def Check_Datas(
    block,
    transaction,
    custom_current_time=None,
    custom_balance=None,
    custom_sequence_number=None,
):
    """
    Check if the transaction datas are valid
    """

    balance = (GetBalance(block, transaction.fromUser)
               if custom_balance is None else custom_balance)
    if balance >= (float(transaction.amount) +
                   float(transaction.transaction_fee)):
        logger.info("Balance is valid")
    else:
        return False

    if not transaction.amount < block.minumum_transfer_amount:
        logger.info("Minimum transfer amount is reached")
    else:
        return False

    if not transaction.transaction_fee < block.transaction_fee:
        logger.info("Transaction fee is reached")
    else:
        return False


    for already_tx in block.pendingTransaction + block.validating_list:
        if already_tx.signature == transaction.signature:
            return False
    logger.info("Transaction is new")

    for tx in block.pendingTransaction + block.validating_list:
        if (tx.fromUser == transaction.fromUser
                and tx.signature != transaction.signature):
            logger.info("Multiple transaction in one account")
            return False

    get_sequance_number = (GetSequanceNumber(transaction.fromUser)
                           if custom_sequence_number is None else
                           custom_sequence_number)
    if transaction.sequance_number == (get_sequance_number + 1):
        logger.info("Sequance number is valid")
    else:
        return False

    current_time = (int(time.time())
                    if custom_current_time is None else custom_current_time)
    if not (current_time -
            transaction.transaction_time) > block.transaction_delay_time:
        logger.info("Transaction time is valid")
    else:
        return False

    return True