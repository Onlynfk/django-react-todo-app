    // Simple list
    new Sortable(example5, {
        handle: '.handle', // handle's class
        animation: 150
    });
    new Sortable(example2Left, {
        group: 'shared' , // set both lists to same group
        animation: 150
    });

    new Sortable(example2Right, {
        group: 'shared',
        animation: 150
    });