import {
  AppBar,
  Toolbar,
  IconButton,
  Typography,
  Stack,
  Button,
  Menu,
  MenuItem,
} from "@mui/material";
import CatchingPokemonIcon from "@mui/icons-material/CatchingPokemon";
import { useState } from "react";
import { Link } from "react-router-dom"; 

export const MuiNavbar = () => {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);
  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) =>
    setAnchorEl(event.currentTarget);

  const handleClose=()=>{
    setAnchorEl(null)
  }
  return (
    <AppBar position="fixed" className="navbar">
      <Toolbar>
        <IconButton size="large" edge="start" color="inherit" aria-label="logo">
          <CatchingPokemonIcon />
        </IconButton>
        <Typography
          variant="h6"
          component="div"
          align="left"
          sx={{ flexGrow: 1 }}
        >
          Pokemon
        </Typography>
        <Stack direction="row" spacing={2}>
          <Button
            color="inherit"
            id="books-menu"
            onClick={handleClick}
            aria-controls={open ? "books-menu" : undefined}
            aria-haspopup="true"
            aria-expanded={open ? "true" : undefined}
            
          >
            Books
          </Button>
          <Button color="inherit">Borrowing</Button>
          <Button color="inherit">Sales</Button>
          <Button color="inherit">About</Button>
          <Button color="inherit">My Account</Button>
        </Stack>
        <Menu id="books-menu" anchorEl={anchorEl} open={open} MenuListProps={{'aria-labelledby': 'books-button'}} onClose={handleClose}>
          <MenuItem onClick={handleClose}>Search by Author</MenuItem>
          <MenuItem onClick={handleClose}>All Books</MenuItem>
        </Menu>
      </Toolbar>
    </AppBar>
  );
};
