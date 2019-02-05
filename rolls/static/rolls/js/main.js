var accountBalance = 100;


function withdrawMoney(amountToWithdraw){
  var newBalance = accountBalance - amountToWithdraw;
  accountBalance = newBalance;
  return amountToWithdraw;
}

console.log('withdraw amount:', withdrawMoney(50));
console.log('new balance', accountBalance);
