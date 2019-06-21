# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Cause(models.Model):  # LEADINGCAUSESOFDEATH.csv
    created_at = models.DateTimeField(default=timezone.now)
    state_code = models.CharField(max_length=255, default=None)   # State_FIPS_Code
    state_name = models.CharField(max_length=255, default=None)   # CHSI_State_Name
    county_name = models.CharField(max_length=255, default=None)  # CHSI_County_Name
    county_code = models.CharField(max_length=255, default=None)  # County_FIPS_Code
    strata_id = models.CharField(max_length=255, default=None)    # Strata_ID_Number
    # 'default=None' wouldn't be something I actually do freely in production.
    # I am doing that here to simplify things for myself upon importing the actual csv

    injury = models.CharField(max_length=255, default='-1111')     # B_Wh_Injury
    cancer = models.CharField(max_length=255, default='-1111')     # B_Wh_Cancer
    homicide = models.CharField(max_length=255, default='-1111')   # B_Wh_Homicide
    suicide = models.CharField(max_length=255, default='-1111')    # C_Wh_Suicide
    hiv = models.CharField(max_length=255, default='-1111')        # D_Wh_HIV
    time_span = models.CharField(max_length=255, default='-1111')  # LCD_Time_Span (survey dates?)
    # I am setting these all to charfields not integers to save time;
    # these are probably fine as integers, but I don't want to risk it.
    # I also only picked a few fields from the csv to keep it simple & readable for my example.
    # I assume there would be foreign keys in here pointing to locations or some other data.
    #

    def __str__(self):
        return '{} - {}'.format(self.state_name, self.county_name)

