﻿#common objects
objLoginContinueButton="xpath=.//*[@id='wrapper']//a[contains(.,'Continue')]"
objLoginContinueButton1="xpath=.//*[@id='wrapper']/div/div/div[2]/div[1]/div/div[3]/div[2]/div/div/a"
objLoginAgreeCheckbox="xpath =.//*[@id='agree']"
objLoginDoneButton ="xpath =.//*[@id='wrapper']//a[contains(.,'Done')]"
oblLoginPageAccountSelected ="xpath = .//*[@id='wrapper']//span[contains(.,'3 accounts selected')]"
objLoginPageMonthDefaultSelection ="xpath = .//*[@id='wrapper']//li[@class='button plain selected'][contains(.,'1mo.')]"
objLoginPage6thMonthSelection = "xpath =.//*[@id='wrapper']//li[@class='button plain'][contains(.,'6mos.')]"
objOverviewDateIconOpen ="xpath = .//*[@id='wrapper']//i[@class='material-icons md-18' and contains(.,'expand_more')]"
objOverviewDateIconClose ="xpath = .//*[@id='wrapper']//i[@class='material-icons md-18' and contains(.,'expand_less')]"
objFromDate ="xpath = .//*[@id='wrapper']//label[contains(.,'From')]//..//following-sibling::div/input[@type='text']"
objToDate="xpath =.//*[@id='wrapper']//label[contains(.,'To')]//..//following-sibling::div/input[@type='text']"
objButtonSixMonths="xpath=.//*[@id='wrapper']//li[@class='button plain' and contains(.,'6mos.')]"
objButtonThreeMonths="xpath=.//*[@id='wrapper']//li[@class='button plain' and contains(.,'3mos.')]"
objButtonOneMonth="xpath=.//*[@id='wrapper']//li[@class='button plain' and contains(.,'1mo.')]"
objOverviewHeaderActive="xpath=.//*[@id='wrapper']//a[@class='overview current']"
objOverviewHeaderInActive="xpath=.//*[@id='wrapper']//a[@class='overview']"
objTagsHeaderInactive="xpath=.//*[@id='wrapper']//a[@class='tags']"
objTagsHeaderActive="xpath=.//*[@id='wrapper']/div//a[@class='tags current']"
objFinancialStatusHeaderInactive="xpath=.//*[@id='wrapper']//a[@class='financial_status']"
objAssessmentTimePeriodEnd="xpath=.//*[@id='wrapper']/div/div[2]/div[@class='date-header']/span[2]"
objAssessmentTimePeriodStart="xpath=.//*[@id='wrapper']/div/div[2]/div[@class='date-header']/span[1]"
objZeroIncomeMessage="xpath=.//*[@id='wrapper']//span/div/div//div[contains(.,'close')]/div[contains(.,'There is no income for selected time period')]"
objZeroExpensesMessage="xpath=.//*[@id='wrapper']//span/div/div//div[contains(.,'close')]/div[contains(.,'There are no expenses for selected time period')]"
objHeading1="xpath=.//*[@id='wrapper']//h2[contains(.,'Income')]"
objHeading2="xpath=.//*[@id='wrapper']//h2[contains(.,'Expenses')]"
objCategorySalary="xpath=.//*[@id='wrapper']//div[2]/div[2]/div[contains(.,'Salary and pension income')]"
objCategoryInvstmt="xpath=.//*[@id='wrapper']//div[2]/div[2]/div[contains(.,'Investment')]"
objCategoryFinInstt="xpath=.//*[@id='wrapper']//div[2]/div[2]/div[contains(.,'FinancialInstitutes')]"
objCategoryResidence="xpath=.//*[@id='wrapper']//div[2]/div[2]/div[contains(.,'Residence')]"
objCategoryCarsandTraffic="xpath=.//*[@id='wrapper']//div[2]/div[2]/div[contains(.,'Car and Traffic')]"
objCategoryFoodandShop="xpath=.//*[@id='wrapper']//div[2]/div[2]/div[contains(.,'Food and groceries shopping')]"
objCategoryHobbies="xpath=.//*[@id='wrapper']//div[2]/div[2]/div[contains(.,'Hobbies and Recreation')]"
objCategoryBills="xpath=.//*[@id='wrapper']//div[2]/div[2]/div[contains(.,'Bills')]"
objTotalIncome="xpath=.//*[@id='wrapper']//div[@class='income']//div[@class='amount']/span"
objTotalIncomeAndroid="xpath=.//*[@id='wrapper']//div[@class='income']//div[@class='amount']"
objTotalExpenses="xpath=.//*[@id='wrapper']//h2[contains(.,'Expenses')]//span[@is='null']"
objTotalExpensesAndroid="xpath=.//*[@id='wrapper']//div[@class='expenses']//div[@class='amount']"
objIncomeInHighlights="xpath=.//*[@id='wrapper']//div[contains(.,'Income')]/a/div[@class='amount__value']/span[@is='null']"
objExpensesInHighlights="xpath=.//*[@id='wrapper']//div[contains(.,'Expenses')]/a/div[@class='amount__value']/span[@is='null']"
objMoneyLeftInHighlights="xpath=.//*[@id='wrapper']//div[contains(.,'Money Left')]//div[@class='amount__value amount__value--positive']/span[@is='null']"
objComparisonCheckbox="xpath=.//*[@id='wrapper']//input[@type='checkbox']"
objDateControl="xpath=.//*[@id='wrapper']//label[contains(.,'To')]"

objOverviewIncome="xpath=.//*[@id='wrapper']//h2[contains(.,'Income')]"
objOverviewIncomeInvestmentCat="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Investment')]"
objOverviewIncomeInvestShareSubCat="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Investment')]//ancestor::div[contains(@class,'category list-item-expanded')]//div[@class='title' and contains(.,'Shares')]"
objOverviewIncomeTags="xpath=.//*[@id='wrapper']//div[@class='subcategory list-item-expanded list-item']//div[@class='list-item-content']//div[@class='transaction income list-item']/a//div[@class='beneficiary']//div[@class='tag']"
objOverviewInvestShareFirstTransaction="xpath=//div[@class='transactions list-view']/div[1]/a[@class='list-item-content']"
objTransactionWindowAddTag="xpath=.//*[@id='wrapper']//div[@class='autocomplete_field']/form/input[@placeholder='Add tag']"
objTransactionWindowAddButton="xpath=.//*[@id='wrapper']//div[@class='autocomplete_field']/form/input[@value='Add']"
objTransactionWindowAddedTag="xpath=.//*[@id='wrapper']//div[@class='autocomplete_field']/a[@class='tag removable']"
objTransactionWindowTagExist="xpath=//div[@class='rc-tooltip-inner']//li[contains(.,'This tag is already present')]"
objTransactionWindowTagName="xpath=.//*[@id='wrapper']//div[@class='autocomplete_field']/a[@class='tag removable' and contains(.,'NewTag')]"
objTransactionWindowCloseButton="xpath=.//*[@id='wrapper']//div/a/i[contains(.,'close')]"
objTransactionWindowViewAllTagsLink="xpath=html/body//a[contains(.,'View all tags')]"
objTransactionWindowDeleteButton="xpath=html/body//a[contains(.,'Delete')]"
objTagsSubCategaoriesNewTag="xpath=.//*[@id='wrapper']//div[@class='category list-item-expanded list-item']//div[contains(.,'NewTag')]//..//div[@class='subcategory list-item-collapsed list-item']"
objTagFirstTransaction="xpath=.//*[@id='wrapper']//div[1][@class='subcategory list-item-expanded list-item']/div[@class='list-item-content']//div[1]/a"

objAccountsSelectionLink="xpath=.//*[@id='wrapper']//span[contains(.,'3 accounts selected')]"


objSavingsAcc1="xpath=.//*[@id='wrapper']//span[@class='title' and contains(.,'Savings Account #1')]"
objSavingsAcc2="xpath=.//*[@id='wrapper']//span[@class='title' and contains(.,'Savings Account #2')]"
objSavingsAcc3="xpath=.//*[@id='wrapper']//span[@class='title' and contains(.,'Savings Account #3')]"
objSelectedSavingsAcc3="xpath=.//*[@id='wrapper']//div[@class='account selected']/span[contains(.,'Savings Account #3')]"
objUnselectedSavingsAcc3="xpath=.//*[@id='wrapper']//div[@class='account']/span[contains(.,'Savings Account #3')]"
objSvgAcc3AmtTop="xpath=.//*[@id='wrapper']//div[@class='account active-accounts']/span[contains(.,'Savings Account #3')]//..//span[@class='balance']/span"
objTwoAcctSelctedAmtTop="xpath=.//*[@id='wrapper']//div[@class='account active-accounts']/span[contains(.,'2 accounts selected')]//..//span[@class='balance']/span"

objAccTotalSelectedAmt="xpath=.//*[@id='wrapper']//span[contains(.,'accounts selected')]//..//span[@class='balance']/span"
objSavingsAcc1Amt="xpath=.//*[@id='wrapper']//div[@class='account-dropdown']//span[contains(.,'Savings Account #1')]//..//span[@class='balance']/span"
objSavingsAcc2Amt="xpath=.//*[@id='wrapper']//div[@class='account-dropdown']//span[contains(.,'Savings Account #2')]//..//span[@class='balance']/span"
objSavingsAcc3Amt="xpath=.//*[@id='wrapper']//div[@class='account-dropdown']//span[contains(.,'Savings Account #3')]//..//span[@class='balance']/span"
objHeaderSelectedSavingsAcc3="xpath=.//*[@id='wrapper']//span[@class='title']/span[contains(.,'Savings Account #3')]"
objHeaderSelectedSavingsAcc2="xpath=.//*[@id='wrapper']//span[@class='title']/span[contains(.,'Savings Account #2')]"
objHeaderSelectedSavingsAcc1="xpath=.//*[@id='wrapper']//span[@class='title']/span[contains(.,'Savings Account #1')]"
objNoAccountSelected="xpath=.//*[@id='wrapper']//span[@class='title']/span[contains(.,'No accounts selected')]"
objNoTxnMsg="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'You have no transactions for selected time period')]"
objZeroBalance="xpath=.//*[@id='wrapper']//span[@class='balance']/span[contains(.,'€0.00')]"
objSharesIncome="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Shares')]//..//div[@class='amount']/span"
objPropertyIncome="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Property')]//..//div[@class='amount']/span"
objInterestIncome="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Interest')]//..//div[@class='amount']/span"
objArrearsIncome="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Arrears')]//..//div[@class='amount']/span"
objIncentiveIncome="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Incentive')]//..//div[@class='amount']/span"
objWagesIncome="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Wages')]//..//div[@class='amount']/span"
objGamesExpense="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Games Accesories')]//..//div[@class='amount']/span"
objRestrauExpense="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Cafes and Restaurants')]//..//div[@class='amount']/span"
objNovelsExpense="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Novels')]//..//div[@class='amount']/span"
objNovelsExpenseAndroid="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Novels')]//..//div[@class='amount']"
objRentExpense="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Rent')]//..//div[@class='amount']/span"
objRentExpenseAndroid="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Rent')]//..//div[@class='amount']"
objFuelsExpense="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Fuels')]//..//div[@class='amount']/span"
objGroceryExpense="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Grocery stores and supermarkets')]//..//div[@class='amount']/span"
objGroceryExpenseAndroid="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Grocery stores and supermarkets')]//..//div[@class='amount']"
objKiosksExpense="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Kiosks')]//..//div[@class='amount']/span"
objKiosksExpenseAndroid="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Kiosks')]//..//div[@class='amount']"
objElectricExpense="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Electric')]//..//div[@class='amount']/span"
objPropertyTaxExpense="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'Property Tax')]//..//div[@class='amount']/span"
objInvestmentIncome="xpath=.//*[@id='wrapper']//div[contains(.,'Investment')]/div[@class='amount']/span[@is='null']"
objInvestmentIncomeAndroid="xpath=.//*[@id='wrapper']//div[contains(.,'Investment')]/div[@class='amount']"
objSalaryAndPensionIncome="xpath=.//*[@id='wrapper']//div[contains(.,'Salary and pension income')]/div[@class='amount']/span[@is='null']"
objSalaryAndPensionIncomeAndroid="xpath=.//*[@id='wrapper']//div[contains(.,'Salary and pension income')]/div[@class='amount']"
objFinancialInstitutesIncome="xpath=.//*[@id='wrapper']//div[contains(.,'FinancialInstitutes')]/div[@class='amount']/span[@is='null']"
objFinancialInstitutesIncomeAndroid="xpath=.//*[@id='wrapper']//div[contains(.,'FinancialInstitutes')]/div[@class='amount']"
objHobbiesExpenses="xpath=.//*[@id='wrapper']//div[contains(.,'Hobbies and Recreation')]/div[@class='amount']/span[@is='null']"
objHobbiesExpensesAndroid="xpath=.//*[@id='wrapper']//div[contains(.,'Hobbies and Recreation')]/div[@class='amount']"
objResidenceExpenses="xpath=.//*[@id='wrapper']//div[contains(.,'Residence')]/div[@class='amount']/span[@is='null']"
objResidenceExpensesAndroid="xpath=.//*[@id='wrapper']//div[contains(.,'Residence')]/div[@class='amount']"
objCarandTrafficExpenses="xpath=.//*[@id='wrapper']//div[contains(.,'Car and Traffic')]/div[@class='amount']/span[@is='null']"
objCarandTrafficExpensesAndroid="xpath=.//*[@id='wrapper']//div[contains(.,'Car and Traffic')]/div[@class='amount']"
objBillsExpenses="xpath=.//*[@id='wrapper']//div[contains(.,'Bills')]/div[@class='amount']/span[@is='null']"
objBillsExpensesAndroid="xpath=.//*[@id='wrapper']//div[contains(.,'Bills')]/div[@class='amount']"
objGroceryExpenses="xpath=.//*[@id='wrapper']//div[contains(.,'Food and groceries shopping')]/div[@class='amount']/span[@is='null']"
objGroceryExpensesAndroid="xpath=.//*[@id='wrapper']//div[contains(.,'Food and groceries shopping')]/div[@class='amount']"

objPopupTxnHeader="xpath=.//*[@id='wrapper']//h1[@class='overlay-title' and contains(.,'Transaction')]"
objPopupTxnAmt="xpath=.//*[@id='wrapper']//p[@class='amount']/span[@is='null']"
objPopupTxnAmtAndroid="xpath=.//*[@id='wrapper']//p[@class='amount']"
objPopupTxnBeneficiary="xpath=.//*[@id='wrapper']//p[@class='to']"
objPopupClose="xpath=.//*[@id='wrapper']//a[@class='close close_x']"

objTxnTags="xpath=.//*[@id='wrapper']//div[1]/a//div[@Class='tag']"

objExpensesTxnBeneficiaries="xpath=.//*[@id='wrapper']//div[@class='subcategory list-item-expanded list-item']//div[@class='beneficiary']"
objExpensesTxnBeneficiariesxpath=".//*[@id='wrapper']//div[@class='subcategory list-item-expanded list-item']//div[@class='beneficiary']"
objMostExpensesBenefxpath=".//*[@id='wrapper']//span[contains(.,'Most expenses')]/div//div[@class='beneficiary']"	

objExpensesGamesTxnBeneficiaryxpath=".//*[@id='wrapper']//div[@class='list-item-toggle' and contains(.,'Games Accesories')]//..//following-sibling::div[@class='list-item-content']//div[@class='transaction expenses list-item']//div[@class='beneficiary']"
objExpensesRestrauTxnBeneficiaryxpath=".//*[@id='wrapper']//div[@class='list-item-toggle' and contains(.,'Cafes and Restaurants')]//..//following-sibling::div[@class='list-item-content']//div[@class='transaction expenses list-item']//div[@class='beneficiary']"
objExpensesNovelsTxnBeneficiaryxpath=".//*[@id='wrapper']//div[@class='list-item-toggle' and contains(.,'Novels')]//..//following-sibling::div[@class='list-item-content']//div[@class='transaction expenses list-item']//div[@class='beneficiary']"
objExpensesRentTxnBeneficiaryxpath=".//*[@id='wrapper']//div[@class='list-item-toggle' and contains(.,'Rent')]//..//following-sibling::div[@class='list-item-content']//div[@class='transaction expenses list-item']//div[@class='beneficiary']"
objExpensesFuelsTxnBeneficiaryxpath=".//*[@id='wrapper']//div[@class='list-item-toggle' and contains(.,'Fuels')]//..//following-sibling::div[@class='list-item-content']//div[@class='transaction expenses list-item']//div[@class='beneficiary']"
objExpensesElectricTxnBeneficiaryxpath=".//*[@id='wrapper']//div[@class='list-item-toggle' and contains(.,'Electric')]//..//following-sibling::div[@class='list-item-content']//div[@class='transaction expenses list-item']//div[@class='beneficiary']"
objExpensesPropertyTaxTxnBeneficiaryxpath=".//*[@id='wrapper']//div[@class='list-item-toggle' and contains(.,'Property Tax')]//..//following-sibling::div[@class='list-item-content']//div[@class='transaction expenses list-item']//div[@class='beneficiary']"
objExpensesGrcryTaxTxnBeneficiaryxpath=".//*[@id='wrapper']//div[@class='list-item-toggle' and contains(.,'Grocery stores')]//..//following-sibling::div[@class='list-item-content']//div[@class='transaction expenses list-item']//div[@class='beneficiary']"
objExpensesKiosksTaxTxnBeneficiaryxpath=".//*[@id='wrapper']//div[@class='list-item-toggle' and contains(.,'Kiosks')]//..//following-sibling::div[@class='list-item-content']//div[@class='transaction expenses list-item']//div[@class='beneficiary']"



objOverviewCatAutomation="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'TESTAUTOMATION')]"
objOverviewSubCatTestPFM="xpath=.//*[@id='wrapper']//div[@class='title' and contains(.,'TESTPFM')]"
objTransactionChangeCategory="xpath=.//*[@id='wrapper']//a[@class='change-category-split']/span[contains(.,'Change category')]"
objBiggestTransactionLabel="xpath =.//*[@id='wrapper']//h2[contains(.,'Biggest expenses')]"
objTopTabMobile = "xpath =.//*[@id='wrapper']//span[contains(.,'Top')]"
objBiggestTransactionLabelMobile="xpath =.//*[@id='wrapper']//h2[contains(.,'Biggest transactions')]"


#Time Based Comparision
objTimeBasedComparisonSectionHeading="xpath=.//*[@id='wrapper']//h2[contains(.,'Time based Comparison')]"
objComareToDropdown="xpath=.//*[@id='dropdown']"
objCompareToDropdownYearSelection="xpath=.//*[@id='dropdown']//option[@Value='previous_year' and contains(.,'Previous Year')]"
objCalender = "xpath = .//*[@id='wrapper']//li[@class='button plain selected']"
objTransactionSplitButton = "xpath =.//*[@id='wrapper']//a[@class='change-category-split']/span[contains(.,'Split')]"
objTransactionSplitDialogBackButton = "xpath = .//*[@id='wrapper']//h1//i[@class= 'material-icons md-36']"
objTransactionSplitDialogHeader = "xpath = .//*[@id='wrapper']//h1[contains(.,'Split Transaction')]"
objTransactionSplitDialogCloseButton = "xpath = .//*[@id='wrapper']//i[@class='material-icons md-36'][contains(.,'close')]"
objTransactionSplitDialogSplitButton = "xpath = .//*[@id='wrapper']//input[@value='Split']"
objTransactionSplitDialogAmountTextBox = "xpath = .//*[@id='wrapper']//input[@placeholder='Enter amount']"
objTransactionSplitDialogAmount = "xpath = .//*[@id='wrapper']//div[@class='category__amount']/span"

#Monthly Budget
objSetSubcategoryBudgetWindowCloseICon="xpath=.//*[@id='wrapper']//a[@class='close close_x']/i[@class='material-icons md-36' and contains(.,'close')]"
objSubcategoryBudgetWindowCurrentLabel="xpath=.//*[@id='wrapper']//div[@class='category__manage__budget']//span[@class='category__month' and contains(.,'Current')]"
objSetSubcategoryBudgetWindowNoBudgetLabel="xpath=.//*[@id='wrapper']//div[@class='category__manage__budget']//span[@class='category__monthly__budget' and contains(.,'No budget')]"
objSetSubcategoryBudgetWindowCurrentMonthBudget="xpath=.//*[@id='wrapper']//div[@class='category__manage__budget']//span[@class='category__no__budget']"
objSetSubcategoryBudgetWindowSetBudgetButton="xpath=.//*[@id='wrapper']//div[@class='overlay-content']//div[@class='adjust__category']"
objSetSubcategoryBudgetWindowLeftArrowIcon="xpath=.//*[@id='wrapper']//div//..//h1//i[@class='material-icons md-36']"
objSetBudgetIon = "xpath=.//*[@id='wrapper']//div[@class='adjust__category']//span[@class='adjust__category__text' and contains(.,'Set budget')]"
objRemoveBudgetButton="xpath=.//*[@id='wrapper']//div[@class='adjust__category']//i[@class='material-icons' and contains(.,'delete')]"
objRemoveBudgetToolTip="xpath=.//div//div[@class='rc-tooltip-inner']/ul//a[contains(.,'Delete')]"
objAdjustBudgetButton="xpath=.//*[@id='wrapper']//div[@class='adjust__category']//span[@class='adjust__category__text' and contains(.,'Adjust Budget')]"
objSetSubcategoryBudgetWindowCurrentLabel = "xpath=.//*[@id='wrapper']//div[@class='overview']//div[@class='category__display__splits']//span[@class='category__month' and contains(.,'Current')]"
objSetSubcategoryBudgetWindowMonthlyBudgetAmount = "xpath=.//*[@id='wrapper']//div[@class='overview']//div[@class='category__display__splits']//span[@class='category__monthly__budget' and contains(.,'€0.00')]"
objSetSubcategoryBudgetWindowMonthlyExpenseAmount = "xpath=.//*[@id='wrapper']//div[@class='overlay open setcategory-window']//div[@class='overlay open setcategory-window']//div[@class='category__display__splits']//span[@class='category__set__budget']"
objSetSubcategoryBudgetWindowProgressLine ="xpath=.//*[@id='wrapper']//div[@class='overview']//div[@class='bar']"
objSetSubcategoryBudgetWindowMinusSign ="xpath=.//*[@id='wrapper']//div[@class='addSubtractBudgetamount']/span[@class='subtract' and contains(.,'-')]"
objSetSubcategoryBudgetWindowPlusSign ="xpath=.//*[@id='wrapper']//div[@class='addSubtractBudgetamount']/span[@class='add' and contains(.,'+')]"
objSetSubcategoryBudgetWindowSetAmount ="xpath=.//*[@id='wrapper']//div[@class='addSubtractBudgetamount']/span[@class='display']"
objSetSubcategoryBudgetWindowDoneButton ="xpath=.//*[@id='wrapper']//div[@class='category__done-button']//input[@class='button' and  @value='Done']"
objSetSubcategoryBudgetWindowMonthlyExpenseAmount1=" xpath=.//*[@id='wrapper']//div[@class='overlay open setcategory-window']//div[@class='overlay open setcategory-window']//div[@class='category__display__splits']/span[2]"
objSetSubCategoryBudgetWIndowSubCategoryExpenseAmount="xpath=.//*[@id='wrapper']//div[@class='overview']//div[@class='category__current__month-div']//span[@class='category__set__budget']/span"
objSetSubCategoryBudgetWIndowSubCategoryBudgetAmount="xpath=.//*[@id='wrapper']//div[@class='overlay open setcategory-window']//div[@class='overlay open setcategory-window']//span[@class='category__monthly__budget']/span"
objSetSubCategoryBudgetWIndowSubCategoryExpenseAmountColor="xpath=html/body//div[2]/div[5]//div/div[3]//div[@class='overlay-content']//div[@class= 'category__display__splits']/span[2]"
objAdjustBudgetWindowSubCategoryExpenseAmount="xpath=.//*[@id='wrapper']//div[@class='overlay-content']/div[@class='category']//div[@class='category__display__splits']//span[@class='category__set__budget']/span[1]"
objAdjustBudgetWindowSubCategoryBudgetAmount="xpath=.//*[@id='wrapper']//div[@class='overlay-content']/div[@class='category']//div[@class='category__display__splits']//span[@class='category__monthly__budget']/span[1]"
objAdjustBudgetWindowSubCategoryRemainingOrOverspentBudgetAmount="xpath=.//*[@id='wrapper']//div[@class='progress']//div[@class='ref']/span/span[1]"
objAdjustBudgetWindowExpenseAmountColor="xpath=.//*[@id='wrapper']//div[@class='overlay-content']/div[@class='category']//div[@class='category__display__splits']//span[@class='category__set__budget']"
objAdjustBudgetWindowProgressBarColor="xpath=.//*[@id='wrapper']//..//div[@class='overlay open setcategory-window']//div[@class='overlay open setcategory-window']//div[3]//..//div[@class='percent']"
ObjSubCategoryWindowExpenseAmount="xpath=.//*[@id='wrapper']//div[@class='category__manage__budget']//span[@class='category__set__budget']/span"
ObjSubCategoryWindowBudgetAmount="xpath=.//*[@id='wrapper']//div[@class='category__manage__budget']//span[@class='category__monthly__budget']//span[1]"
ObjSubCategoryWindowRemainingOrOverspentBudgetAmount="xpath=.//*[@id='wrapper']//div[@class='progress']//div[@class='ref']//span[1]"
ObjSubCategoryWindowProgressBar="xpath=.//*[@id='wrapper']//div[@class='progress']//div[@class='bar']/div[1]"





#Split Transanction

objCalenderExpandMore = "xpath =  .//*[@id='wrapper']//li[@class='button plain']/i[contains(.,'expand_more')]"
objCalenderExpandLess = "xpath =  .//*[@id='wrapper']//li[@class='button plain']/i[contains(.,'today')]"
objTransactionSplitButton = "xpath =.//*[@id='wrapper']//a[@class='change-category-split']/span[contains(.,'Split')]"
objTransactionSplitDialogBackButton = "xpath = .//*[@id='wrapper']//h1//i[@class= 'material-icons md-36']"
objTransactionSplitDialogHeader = "xpath = .//*[@id='wrapper']//h1[contains(.,'Split Transaction')]"
objTransactionSplitDialogCloseButton = "xpath = .//*[@id='wrapper']//i[@class='material-icons md-36'][contains(.,'close')]"
objTransactionSplitDialogSplitButton = "xpath = .//*[@id='wrapper']//input[@value='Split']"
objTransactionSplitDialogAmountTextBox = "xpath = .//*[@id='wrapper']//input[@placeholder='Enter amount']"
objTransactionSplitDialogAmount = "xpath = .//*[@id='wrapper']//div[@class='category__amount']/span"
objTransactionSplitDialogDoneButton = "xpath = .//*[@id='wrapper']//input[@value='Done']"
objTransactionSplitIcon = "xpath = .//*[@id='wrapper']//p[@class='amount']/i[contains(.,'call_split')]"
objTransactionSplitDeleteToolTip = "xpath = .//a[contains(.,'Delete')]"
objTransactionSplitOriginalAmt = "xpath = .//*[@id='wrapper']//div[@class= 'category__original-amount']/span"
objTransactionSplitMoreThan10ErrorMessage = "xpath = .//*[@id='wrapper']//label[contains(.,'** Maximum 10 splits allowed from Parent transaction.')]"
