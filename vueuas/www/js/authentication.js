function findUsefulToken() {
    const permanent = {}
    document.cookie
        .split(';')
        .filter(i => i.indexOf('=') > -1)
        .map(i => i.split('='))
        .filter(i => i.length === 2)
        .forEach(i => permanent[i[0].trim()] = i[1].trim())
    if (!permanent.hasOwnProperty('UserToken'))
        return null
    return permanent.UserToken
}

function keepNewToken(starToken) {
    document.cookie = `UserToken=${starToken}`
}
