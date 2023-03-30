#!/bin/bash

git fetch 

if [[ "${CI_COMMIT_REF_NAME}" =~ "dev"*|"master"* ]];
then
    echo "Son ramas padres, se omite la verificacion!!!"
    exit 0
fi

echo "--->RULE # 1: Checking format for branch name..."
if [[ ! "${CI_COMMIT_REF_NAME}" =~ "Feature/"*|"Hotfix/"*|"Refactor/"*|"dev"*|"master"* ]];
then
    echo "RULE # 1: [ERROR] Invalid naming for branch!"
    exit 1
else
    echo "RULE # 1: Correct Branch name!!!"
fi

echo "--->RULE # 2: Checking commit message format..."
if [[ ! "${CI_COMMIT_MESSAGE}" =~ "Hotfix: "*|"Feature: "*|"Documentation: "*|"Refactor: "* ]];
then
    echo "RULE # 2: [ERROR] Invalid commit message format!"
    exit 1
else
    echo "RULE # 2: Checked successfully!"
fi

LATEST_MASTER_HASH=$(git rev-parse --short=8 HEAD)
LATEST_SHARED_HASH=${CI_COMMIT_SHORT_SHA}

echo "--->RULE # 3: Checking rebase with master..."
if [[ ! $LATEST_MASTER_HASH == $LATEST_SHARED_HASH ]];
then
    echo "RULE # 3: [ERROR] You missed to rebase with master!"
    exit 1
else
    echo "RULE # 3: Checked successfully!"
fi

if [[ ! "${CI_COMMIT_REF_NAME}" =~ "Hotfix/"* ]];
then
    BRANCH_NAME="dev"
else
    BRANCH_NAME="master"
fi


COMMITS_COUNT=$(git log --oneline origin/${CI_COMMIT_REF_NAME} ^origin/${BRANCH_NAME} | wc -l)

echo "--->RULE # 4: Checking for new changes..."
if [[ $COMMITS_COUNT == 0 ]] && [[ ! $CI_COMMIT_REF_NAME == master ]] && [[ ! $CI_COMMIT_REF_NAME == dev ]];
then
    echo "RULE # 4: [ERROR] You need to add new changes!"
    exit 1
else
    echo "RULE # 4: Checked successfully!"
fi

echo "--->RULE # 5: Checking number of commits..."
if [[ $COMMITS_COUNT > 1 ]];
then
    echo "RULE # 5: [ERROR] There must be only one commit!, you have ($COMMITS_COUNT) commits"
    exit 1
else
    echo "RULE # 5: Checked successfully!"
fi

INSERTIONS=$(git diff --shortstat origin/master | sed -E "s/.* ([0-9]+) insertion.*/\1/")
INSERTIONS_NUMBER=9000

echo "--->RULE # 6: Checking number of insertions ($INSERTIONS) < ($INSERTIONS_NUMBER)..."

if (( $INSERTIONS > $INSERTIONS_NUMBER ));
then
    echo "RULE # 6: [ERROR] You exceeded the insertions limit with $INSERTIONS lines!"
    exit 1
else
    echo "RULE # 6: Number of insertions allowed!"
fi

DELETIONS=$(git diff --shortstat origin/master | sed -E "s/.* ([0-9]+) deletion.*/\1/")
DELETIONS_NUMBER=9000

echo "--->RULE # 7: Checking number of deletions ($DELETIONS) < ($DELETIONS_NUMBER)..."
if (( $DELETIONS > $DELETIONS_NUMBER ));
then
    echo "RULE # 7: [ERROR] You exceeded the deletions limit with $DELETIONS lines!"
    exit 1
else
    echo "RULE # 7: Checked successfully!"
fi
