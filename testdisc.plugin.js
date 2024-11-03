function MySearchInput(props) {
    return <input
                type="text"
                placeholder={props.placeholder || "Search..."}
                onChange={props?.onChange}
            />;
}

BdApi.UI.alert(
    "Input Test",
    <MySearchInput
        placeholder="Testing..."
        onChange={event => console.log(event)}
    />
);