def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    return dealer_total <= 21 and player_total < 21
