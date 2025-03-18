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
        <IconButton size="large" edge="start" color="inherit" aria-label="logo" component={Link} to=''>
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
            component={Link} to='Books'
          >
            Books
          </Button>
          <Button color="inherit" component={Link} to='Borrowing'>Borrowing</Button>
          <Button color="inherit" component={Link} to='Sales'>Sales</Button>
          <Button color="inherit" >About</Button>
          <Button color="inherit">My Account</Button>
        </Stack>
        
      </Toolbar>
    </AppBar>
  );
};
